<그래프1>

import csv
import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')

f=open('성 연령별 경제활동인구.csv')
data=list(csv.reader(f))
people=[]
employ=[]
unemploy=[]
x=int(input("전체를 원하시면 1번, 남성의 자료를 원하시면 2번, 여성의 자료를 원하시면 3번을 입력해주세요"))

for i in range(3+(x-1)*7,9+(x-1)*7):
    people.append(int(data[i][3]))
    employ.append(int(data[i][4]))
    unemploy.append(int(data[i][5]))

    
a=['15~19세','20~29세','30~39세','40~49세','50~59세','60세 이상']    
plt.bar(a,people, label='경제활동 인구',color='mediumaquamarine')
plt.plot(a,employ, label='취업자 수', color='navy')
plt.plot(a,unemploy,label='실업자 수',color='salmon')


plt.legend(loc=1)
plt.xlabel('연령')
plt.ylabel('인구수 (천명)')
if x==1 :
    plt.title('연령별 취업자 실업자 현황(전체)')
elif x==2 :
     plt.title('연령별 취업자 실업자 현황(남성)')
elif x==3 :
     plt.title('연령별 취업자 실업자 현황(여성)')
plt.savefig('data.png')
plt.show()

<그래프 2>


import csv
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')

x = int(input('남자와 여자의 실업자 비교를 보고싶으면 1번, 취업자 비교를 보고 싶으면 2번을 입력하세요'))
f=open('성 연령별 경제활동인구.csv')
data=list(csv.reader(f))
man=[]
woman=[]
for i in range(10,16) :
    if x + 1 == 2 :
        man.append(int(data[i][5]))
    if x + 1 == 3 :
        man.append(int(data[i][4]))
        
for i in range(17,23) :
    if x+1==2 :
        woman.append(int(data[i][5]))
    if x + 1 == 3 :
         woman.append(int(data[i][4]))

ind = np.arange(len(man))
width = 0.1

fig, ax = plt.subplots()   
rects1= ax.bar(ind - width/2,man,label='남자', color='skyblue')
rects2= ax.bar(ind+ width/2,woman,label='여자',color='salmon')

plt.legend(loc=1)
plt.xlabel('연령')
plt.ylabel('인구수 (천명)')
if x + 1 == 2 :
        plt.title('연령별 실업자 현황')
if x + 1 == 3 :
        plt.title('연령별 취업자 현황')

ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('15~19세','20~29세','30~39세','40~49세','50~59세','60세 이상'))

def autolabel(rects, xpos='center'):
    xpos = xpos.lower() 
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43} 

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")

plt.show()

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
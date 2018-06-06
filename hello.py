<�׷���1>

import csv
import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')

f=open('�� ���ɺ� ����Ȱ���α�.csv')
data=list(csv.reader(f))
people=[]
employ=[]
unemploy=[]
x=int(input("��ü�� ���Ͻø� 1��, ������ �ڷḦ ���Ͻø� 2��, ������ �ڷḦ ���Ͻø� 3���� �Է����ּ���"))

for i in range(3+(x-1)*7,9+(x-1)*7):
    people.append(int(data[i][3]))
    employ.append(int(data[i][4]))
    unemploy.append(int(data[i][5]))

    
a=['15~19��','20~29��','30~39��','40~49��','50~59��','60�� �̻�']    
plt.bar(a,people, label='����Ȱ�� �α�',color='mediumaquamarine')
plt.plot(a,employ, label='����� ��', color='navy')
plt.plot(a,unemploy,label='�Ǿ��� ��',color='salmon')


plt.legend(loc=1)
plt.xlabel('����')
plt.ylabel('�α��� (õ��)')
if x==1 :
    plt.title('���ɺ� ����� �Ǿ��� ��Ȳ(��ü)')
elif x==2 :
     plt.title('���ɺ� ����� �Ǿ��� ��Ȳ(����)')
elif x==3 :
     plt.title('���ɺ� ����� �Ǿ��� ��Ȳ(����)')
plt.savefig('data.png')
plt.show()

<�׷��� 2>


import csv
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')

x = int(input('���ڿ� ������ �Ǿ��� �񱳸� ��������� 1��, ����� �񱳸� ���� ������ 2���� �Է��ϼ���'))
f=open('�� ���ɺ� ����Ȱ���α�.csv')
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
rects1= ax.bar(ind - width/2,man,label='����', color='skyblue')
rects2= ax.bar(ind+ width/2,woman,label='����',color='salmon')

plt.legend(loc=1)
plt.xlabel('����')
plt.ylabel('�α��� (õ��)')
if x + 1 == 2 :
        plt.title('���ɺ� �Ǿ��� ��Ȳ')
if x + 1 == 3 :
        plt.title('���ɺ� ����� ��Ȳ')

ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('15~19��','20~29��','30~39��','40~49��','50~59��','60�� �̻�'))

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
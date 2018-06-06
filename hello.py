
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
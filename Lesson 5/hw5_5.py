from random import randint
#try:
'''
with open(r'file_hw5_5.txt', 'w')as f:
    some_list=[str(randint(0,100)) for _ in range(10)]
    some_str=' '.join(some_list)
    f.write(some_str)
print(some_list)
print(some_str)
'''
some_list=[]
sum=0
with open(r'file_hw5_5.txt') as f:
    data=f.read()
    some_list=data.split()
    #print(some_list)
for x in some_list:
    sum+=int(x)
    #print(x)#some_list.append(int(x)))
print('Сумма чисел равна {}'.format(sum))

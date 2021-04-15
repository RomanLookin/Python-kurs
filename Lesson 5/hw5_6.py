new_list=[]
list2=[]
dict_l={}
sum=0
with open(r'file_hw5_6.txt') as f:
    for line in f:
        new_list.append(line.split(':'))
for zap in new_list:
#    print(zap[0])
    list2=zap[1].split(' ')
    #print(zap[1].split(' '))
    for i in list2:
        poz=i.find('(')
        if poz != -1:
            sum=sum+int(i[:poz])
#        print('poz (='+str(i.find('(')))
#        print(i)
    dict_l[zap[0]]=sum
    sum=0
print(dict_l)
        



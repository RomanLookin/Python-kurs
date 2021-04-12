#Определить элементы списка, не имеющие повторений
some_list=[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
some_list2=[]

some_list2=[some_list[el] for el in range(len(some_list)) if some_list.count(some_list[el]) == 1]

'''
i=0
while i<len(some_list):
    if some_list.count(some_list[i]) == 1:   
        some_list2.append(some_list[i])
    i=i+1
'''
print(some_list)
print(some_list2)


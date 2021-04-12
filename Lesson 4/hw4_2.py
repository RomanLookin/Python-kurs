import random
some_list=[random.randint(0,300) for _ in range(13)]
some_list2=[]
some_list2.append([some_list[el] for el in range(1,len(some_list)) if some_list[el] > some_list[el-1]])
print(some_list)
print(some_list2)

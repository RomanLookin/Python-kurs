from functools import reduce
some_list=[num for num in range(100, 107) if num%2 == 0]
proizv_all=reduce(lambda x,y: x*y, some_list)
print(some_list)
print(proizv_all)


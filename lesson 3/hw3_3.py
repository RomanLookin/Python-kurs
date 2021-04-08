def my_func(a, b, c):
    numb=[a,b,c]
    min_num=min(numb)
    sum=0
    for i in range(3):
        if numb[i]!=min_num:
            sum+=numb[i]
    return sum
    
some_list=input('введите три числа').split()
for i in range(3):
    some_list[i]=int(some_list[i])
print(some_list)
print('сумма наибольших двух чисел= ', my_func(some_list[0],some_list[1],some_list[2]))
    

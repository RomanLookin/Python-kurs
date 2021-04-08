def func_sum(sum_first, *args):
    return sum_first+sum(*args)

summa=0
per_exit=True
while per_exit:
    some_str=input('Введите строку чисел через пробел (q - выход):').split()
    i=0
    some_str2=[]
    while i < len(some_str):
        if some_str[i].isdecimal():
            some_str2.append(int(some_str[i]))
        else:
            per_exit = False
            break
        i+=1
    summa = func_sum(summa, some_str2)
    print('сумма введенных чисел равна {}'.format(summa))


def my_func(x, y):
    #return x**y
    num=1
    y=-y
    while y!=0:
        num=num/x
        y=y-1
    return num

while True:
    strk=input('Введите два числа через пробел (q - выход):').split()
    if strk[0] is 'q': # выход
        break
    else:
        strk[0]=int(strk[0])
        strk[1]=int(strk[1])
        print(my_func(strk[0],strk[1]))

    

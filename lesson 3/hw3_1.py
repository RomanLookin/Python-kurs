# функцияпринимает два числа и выполняет их деление.
#числа запрашивать у пользователя, предусмотреть деление на ноль
def func_div(num1, num2):
    return num1/num2
while True:
    strk=input('Введите два числа через пробел (q - выход):').split()
    if strk[0] is 'q':
        break
    elif strk[1]=='0':
        print('Второе число не должно быть равно нулю')
    else:
        strk[0]=int(strk[0])
        strk[1]=int(strk[1])
        print(func_div(strk[0],strk[1]))

    

        


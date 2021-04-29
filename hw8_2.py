class OwnError(Exception):
    def __init__(self, txt):
        self.txt=txt

    
inp_num1=input('Введите первое число (q-выход):')
while inp_num1 != 'q':
    try:
        inp_num2=input('Введите второе число (не 0):')
        
        if inp_num2 == '0':
            raise OwnError('Второе число д.б. не равно 0')
        elif inp_num2.isdigit()==False:
            raise OwnError('Второе д.б. число')
        elif inp_num1.isdigit()==False:
            raise OwnError('Первое д.б. число')
        else:
            inp_num1,inp_num2=int(inp_num1),int(inp_num2)
            print(inp_num1/inp_num2)
    except OwnError as err:
        print(err)
    inp_num1=input('Введите первое число (q-выход):')

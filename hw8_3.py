class OwnError(Exception):
    def __init__(self, txt):
        self.txt=txt
msv=[]
inp_num=input('Введите число (stop-выход):')
while inp_num != 'stop':
    try:
        if inp_num.isdigit(): 
            inp_num=int(inp_num)
            msv.append(inp_num)
        else: raise OwnError('Введено не число')
    except OwnError as err:
        print(err)
    inp_num=input('Введите число (stop-выход):')
    
print(msv)

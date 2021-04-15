data=[]
sum=0
num_pers=0
try:
    with open(r'file_hw5_3.txt', encoding='utf-8') as f:
        for line in f:
            #print(line,end='')
            data=line.split()
            sum+=int(data[1])
            num_pers+=1
            if int(data[1]) < 20000:
                print('У '+data[0]+' оклад менее 20000 руб')
        print('средняя величина дохода сотрудников {}'.format(sum/num_pers))
        
except IOError:
        print('No such file in directory')

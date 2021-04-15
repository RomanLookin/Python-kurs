data=[]
try:
    with open(r'file_hw5_2.txt', encoding='utf-8') as f:
        data=f.readlines()
        print(data)
        print('количество строк - {}'.format(len(data)))
        print('количество строк в 1 строке {}'.format(len(data[0].split())))
        print('количество строк в 2 строке {}'.format(len(data[1].split())))
        print('количество строк в 3 строке {}'.format(len(data[2].split())))
except IOError:
        print('No such file in directory')

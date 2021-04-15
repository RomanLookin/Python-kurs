with open('file_hw5_1.txt', 'x') as f:
    str=input('Введите данные для записи в файл')
    while str!='q':
        f.write(str+'\n')
        str=input('Введите данные для записи в файл (q-выход)')
    

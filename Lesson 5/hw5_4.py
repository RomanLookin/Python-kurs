data=[]
some_dict={'One':'Один',
           'Two':'Два',
           'Three':'Три',
           'Four':'Четыре'
    }
try:
    with open(r'file_hw5_4.txt', 'r' ,encoding='utf-8') as f:
        #data=f.readlines()
        for line in f:
            data.append(line.split(' '))
            #data.append(line.replace('\n',''))
            #print(line.replace('\n',''))
            
        #print(len(data))
    #
    for key in some_dict.keys():
        for zap in data:
            if key == zap[0]:
                zap[0]=some_dict[key]
                break
    with open(r'file_hw5_4.txt', 'a' ,encoding='utf-8') as f:
        f.write('\n')
        for it in data:
            f.write(' '.join(it))
        
except IOError:
        print('No such file in directory')

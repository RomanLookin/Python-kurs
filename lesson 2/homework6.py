name=input('Введите название товара (exit=выход):')
list_tuple=[]
some_list=[]
iter=0
while name != 'exit':
    cena=int(input('Введите цену товара:'))
    colic=input('Введите количество товара:')
    if colic.isdigit():
        colic=int(colic)
    else:
        print('Введите целое число для количества')
        continue
    izmer=input('Введите единицу измерения товара:')
    some_dict={'название':name,'цена':cena,'количество':colic,'ед':izmer}
    
    list_tuple =(iter+1, some_dict)
    some_list.append(list_tuple)
    iter+=1
    
    name=input('Введите название товара (exit=выход):')
        
print(some_list)
print(some_list[0][1]['название'])
print(len(some_list))
iter = 0
my_dict={}
my_list=[]

while iter < len(some_list):
    my_list.append(some_list[iter][1]['название'])
    iter+=1
my_dict={'название':my_list}
print(my_dict)

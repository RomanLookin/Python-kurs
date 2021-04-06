
some_list=[]

var_input=input('Введите елемент списка:')
while var_input!='exit':#заполняем список
    some_list.append(var_input)
    var_input=input('Введите елемент списка:')

print(some_list)

iter=0
while iter < len(some_list)-1:
    per1=some_list[iter+1]
    some_list[iter+1]=some_list[iter]
    some_list[iter]=per1
    iter=iter+2
print(some_list)

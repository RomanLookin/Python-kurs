#задание 4

var_str=input('enter a positive integer:')
var_max=0
iter=0
while iter<len(var_str):
    if int(var_str[iter])>var_max:
        var_max=int(var_str[iter])
    iter=iter+1
print('максимальное число в '+var_str+': '+str(var_max))

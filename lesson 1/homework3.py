#задание 3
'''
var_int=int(input('enter you integer number:'))
var1=var_int*10+var_int
var2=var_int*100+var1
#n+nn+nn 3+33+33=...   10+1010+101010=...
print('{}+{}+{}={}'.format(var_int,var1,var2,var_int+var1+var2))
'''
# 2
var_str=input('enter you integer number:')
var1=var_str+var_str
var2=var1+var_str
print('{}+{}+{}={}'.format(var_str,var1,var2,int(var_str)+int(var1)+int(var2)))

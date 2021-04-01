#задание 2
var_int=int(input('enter you count seconds:'))
var_hour=var_int//3600
var_min=(var_int-var_hour*3600)//60
var_sec=var_int-var_hour*3600-var_min*60
print('Это соответствует (чч:мм:сс):{}:{}:{}'.format(var_hour,var_min,var_sec))


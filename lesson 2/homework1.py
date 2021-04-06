some_list = [ 1 , 'var', 45.76, '99.34', [ 1223, 'lala']]
print(str(some_list) +' тип- '+str(type(some_list)))
var_iter=0
while var_iter < len(some_list):
    print(str(some_list[var_iter]) + ' тип- '+str(type(some_list[var_iter])))
    var_iter+=1

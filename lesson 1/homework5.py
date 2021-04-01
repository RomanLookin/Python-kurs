#задание 5

var_vir=int(input('Введите выручку фирмы:'))
var_izd=int(input('Введите издержки фирмы:'))
if var_vir > var_izd:
    print('фирма работает в прибыль')
    var_prib=var_vir-var_izd
    print('рентабельность:'+str(var_prib/var_vir))
    var_sotr=int(input('Введите численность сотрудников фирмы:'))
    print('прибыль на одного сотрудника:'+str(var_prib/var_sotr))
else:
    print('фирма работает в убыток')

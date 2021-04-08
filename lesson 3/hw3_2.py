def about_user(name='geekbrains', old_name='gb', year='2021', sity='moskow', email='gb@mail.ru', phone='4951234567'):
    return print('name:{} oldname:{} year:{} sity:{} email:{} phone:{}'.format(name, old_name, year, sity, email, phone))

while True:
    some_str=input('Введите через пробел: имя, фамилию, год рождения, город проживания, email,телефон (q-выход):').strip()
    

    if len(some_str) == 0:
        about_user()
    elif some_str[0] != 'q':
        about_user(some_str[0], some_str[1],some_str[2],some_str[3],some_str[4], some_str[5])
    else:
        break

    

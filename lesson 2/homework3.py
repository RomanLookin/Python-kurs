month=int(input('Введите номер месяца (целое число от 1 до 12):'))

some_list=['зима','весна','лето','осень']
if month == 1 or month == 2 or month == 12:
    print('{}-й месяц это зима'.format(month))
elif 3 <= month <= 5:
    print('{}-й месяц это весна'.format(month))
elif 6 <= month <= 8:
    print('{}-й месяц это лето'.format(month))
elif 9 <= month <= 11:
    print('{}-й месяц это осень'.format(month))
some_dict={1: 'зима',
           2: 'зима',
           3: 'весна',
           4: 'весна',
           5: 'весна',
           6: 'лето',
           7: 'лето',
           8: 'лето',
           9: 'осень',
           10: 'осень',
           11: 'осень',
           12: 'зима',
    }
print('{}-й месяц это {}'.format(month, some_dict.get(month)))

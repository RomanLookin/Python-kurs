some_str='Пользователь вводит строку из нескольких слов разделённых пробелами'#input('Введите строку из нескольких слов:')
some_list=some_str.split()
iter=0
while iter < len(some_list):
    if len(some_list[iter]) > 10:
        some_list[iter]=some_list[iter][:10]
    print(str(iter+1)+' '+some_list[iter])
    iter+=1

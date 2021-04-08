def int_func(text):
    return text.capitalize()

some_str=input('Введите строку из слов, разделенных пробелом').split()
some_str_new=[]
i=0
while i < len(some_str):
    some_str_new.append(int_func(some_str[i]))
    i+=1
print(' '.join(some_str_new))


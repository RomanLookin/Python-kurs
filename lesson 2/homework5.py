my_list = [7, 5, 3, 3, 2]
num=int(input('Введите число:'))
count_list=len(my_list)
iter=0
var=False
while iter < count_list:
    if num > my_list[iter]:
        my_list.insert(iter, num)
        var=True
        break
    iter+=1
if var == False:
    my_list.append(num)
print(my_list)

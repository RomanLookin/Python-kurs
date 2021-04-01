#задание 6

var_prob_a=int(input('Введите количество километров в первый день:'))
var_prob_b=int(input('Введите необходтмое количество километров:'))
var_num_day=1
print('{}-й день:{}'.format(var_num_day,var_prob_a))
while var_prob_a < var_prob_b:
    var_prob_a = var_prob_a*1.1
    var_num_day=var_num_day+1
    print('{}-й день:{:.2f}'.format(var_num_day,var_prob_a))
print('Ответ: на {}-й день спортсмен достиг результата:не менее {} км'.format(var_num_day,var_prob_b))
print('Резельтат {:.2f} км'.format(var_prob_a))
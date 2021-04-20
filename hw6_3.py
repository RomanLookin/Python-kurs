class Worker:
    #name=''
    #surname=''
    #_income={'wage': 0, 'bonus': 0}
    def __init__(self,name,surname,wage,bonus):
        self.name=name
        self.surname=surname
        self._income={'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self,name,surname,wage,bonus):
        super().__init__(name,surname,wage,bonus)
    def get_full_name(self):
        return self.name+" "+self.surname
    def get_total_income(self):
        return self._income['wage']+self._income['bonus']

worker1=Position('roman','lukin',1000,10)
print(worker1.name)
print(worker1.surname)
print(worker1._income['wage'])
print(worker1._income['bonus'])
print('Полное имя сотрудника: '+worker1.get_full_name())
print('Доход сотрудника: '+str(worker1.get_total_income()))

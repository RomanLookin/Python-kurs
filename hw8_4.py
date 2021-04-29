class Orgtech:
    def __init__(self, model_name):
        self.model_name=model_name                
        #self.razrab=razrab
        
sklad={}
podrazd={}
      

class Printer(Orgtech):
    def __init__(self, model_name,count, technologia, color, scorost):#,razrab
        super().__init__(model_name)#,razrab
        self.technologia=technologia
        self.color=color
        self.scorost=scorost
        #self.count=count
        sklad[self.model_name]=int(count) #поступление на склад
    def __str__(self):
        str_out='Модель: '+self.model_name+'\n'+\
                'Технология: '+self.technologia+'\n'+\
                'Количество: '+str(sklad[self.model_name])+' шт.\n'+'-'*10
        return str_out
    def out_to_podr(self,name_podr,count_podr):
        #out_str=''
        for key in sklad.keys():
            if key == self.model_name:
                sklad[self.model_name]-=count_podr
                podrazd[name_podr]=count_podr
                print('**Убираем '+self.model_name+' '+str(count_podr)+'шт со склада')
                break
       
    
#'Изготовитель: '+self.razrab+'\n'+\
#new_str=(input('Введите тип, модель, кол-во')).split(' ') ,'Epson'
printer_1=Printer('Epson','10','Лазерный',True,'600')
printer_2=Printer('HP','15','Струйный',False,'300')
print(printer_1)
print(printer_2)
print(sklad)
printer_1.out_to_podr('distrib',2)
printer_2.out_to_podr('distrib1',3)
print(printer_1)
print(printer_2)
print(sklad)
print(podrazd)
    

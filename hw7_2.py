from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def calc_tkan(self,HV):
        pass
class Palto(Clothes):
    def calc_tkan(self,HV):
        return HV/6.5+0.5
class Kostum(Clothes):
    def calc_tkan(self,HV):
        return 2*HV+0.3

palto=Palto()
kostum=Kostum()
razm_palto=int(input('Введите размер пальто'))
rost_kost=int(input('Введите рост костюма'))
print('Для {} размера пальто понадобится {:.2f}'.format(razm_palto,palto.calc_tkan(razm_palto))+' метров ткани')
print('Для {} размера пальто понадобится {:.2f}'.format(rost_kost,kostum.calc_tkan(rost_kost))+' метров ткани')


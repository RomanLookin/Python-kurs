class Road:
    def calc(self):
        return 25*5*self._length*self._width

massa_asf=Road()
massa_asf._length=float(input('Введите длину дороги:'))
massa_asf._width=float(input('Введите ширину дороги:'))
print('масса асфальта равна: '+str(massa_asf.calc())+' кг')

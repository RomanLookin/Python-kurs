class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed=speed
        self.color=color
        self.name=name
        self.is_police=is_police
    def go(self):
        print(self.name+' поехала')
    def stop(self):
        print(self.name+' остановилась')
    def turn_left(self):
        print(self.name+' повернула на лево')
    def turn_right(self):
        print(self.name+' повернула на право')
    def show_speed(self):
        print('текущая скорость '+self.name+' '+str(self.speed))
class TownCar(Car):
    def show_speed(self):
        if self.speed >60:
            print('превышение скорости '+self.name)
        else:
            print('текущая скорость '+self.name+' '+str(self.speed))
    
lada=Car(50,'red','лада',False)
print(lada.name)
lada.go()
lada.turn_left()
lada.show_speed()
towncar=TownCar(70,'green','bmv',False)
towncar.show_speed()


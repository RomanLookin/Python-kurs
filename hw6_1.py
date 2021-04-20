import time

class TrafficLight:
    #color=red
    #__perem=0
    def __init__(self):
        self._color='red'
        print('Trafficlight in red')
        
    def running(self, color):
        if color == 'red':
            self._color = 'yellow'
            #print(self.__perem)
            return print('TrafficLight in yellow')
        elif color == 'yellow':
            self._color = 'green'
            return print('TrafficLight in green')
        else: 
            self._color = 'red'
            return print('TrafficLight in red')

traffic_light=TrafficLight()
time.sleep(7)
traffic_light.running(traffic_light._color)
time.sleep(2)
traffic_light.running(traffic_light._color)  
time.sleep(7)


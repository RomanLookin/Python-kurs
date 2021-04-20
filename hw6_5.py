class Stationery:
    title='Канцелярские принадлежности'
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')
class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')
class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')
stat=Stationery()
stat.draw()
pen_stat=Pen()
pen_stat.draw()
pens_stat=Pencil()
pens_stat.draw()
handle_stat=Handle()
handle_stat.draw()

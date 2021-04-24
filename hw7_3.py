class Cell:
    def __init__(self, count):
        self.count=count
    def __add__(self,obj):
        return self.count+obj.count
    def __sub__(self, obj):
        rez=self.count-obj.count
        if rez>0:
            return rez
        else:
            return self.count+' должно быть больше '+obj.count
    def __mul__(self,obj):
        return self.count*obj.count
    
    def __mul__(self,obj):
        if obj.count != 0:
            return self.count/obj.count
        else:
            return obj.count+' не должен быть равен нулю'
    def make_order(self, num, num_in_row):
        str=''
        qqq=int(num) // int(num_in_row)
        for _ in range(qqq):
            str+='*'*num_in_row+'\n'
        #qqq2=int(num) - qqq * int(num_in_row)
        str+='*'*(int(num) - qqq * int(num_in_row))#qqq2 
        return str  

cell=Cell(10)
print(cell.make_order(12, 3))
        

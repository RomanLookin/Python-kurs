class Data:
    @classmethod
    def out_dmy(cls, dmy):
        out=dmy.split('-')
        for i in range(len(out)):
            out[i]=int(out[i])
        return out
    @staticmethod
    def valid(out):
        ret=True
        if out[0] <1 or out[0] >31:
            print('data false')
            ret=False
        if out[1] <1 or out[1] >12:
            print('month false')
            ret=False
        if out[2] <0 or out[2] >2021:
            print('year false')
            ret=False
        if ret: print('data valid')
         
        #print(out)

chislo='01-01-2021'
numb=Data.out_dmy(chislo)
print(numb)
Data.valid(numb)

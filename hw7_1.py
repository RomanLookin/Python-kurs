class Matrix:
    def __init__(self, some_list):
        self.mtrx=some_list
    def __str__(self):
        #out_str='x'.join(str(self.mtrx[0]))
        out_str=''
        for i in range(len(self.mtrx)):
            for f in range(len(self.mtrx[0])):
                out_str=out_str+str(self.mtrx[i][f])+' '
            out_str=out_str+'\n' 
        
        return out_str #str(self.mtrx[0])+'\n'+str(self.mtrx[1])
    def __add__(self, obj):
        return [[self.mtrx[i][j]+obj.mtrx[i][j] for j in range(len(self.mtrx[0]))] for i in range(len(self.mtrx))] 

el_matrix=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
el_matrix2=[[11, 12, 13],[14, 15, 16],[17, 18, 19]]
#el_matrix=[[1, 2],[4, 5],[7, 8, 9]]
#el_matrix2=[[11, 12],[14, 15],[17, 18, 19]]

matr=Matrix(el_matrix)
matr2=Matrix(el_matrix2)
new_mtrx=matr+matr2
print(new_mtrx)
#print(matr)

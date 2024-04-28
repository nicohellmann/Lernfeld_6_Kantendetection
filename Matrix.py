from __future__ import annotations


class Matrix:
    # to create a matrix of ones set ones to true
    def __init__(self, matrix:list, ones=False,rows =0, columns=0):
        #rows  = reihe
        #columns= spalte
        if ones:
            matrixones =[]
            for i in range(0,rows):
                helpones = []
                for j in range(0, rows):
                    helpones.append(1)
                matrixones.append(help)

            self.matrix =matrixones
            self.rows = rows
            self.columns = rows

        else:
            self.matrix = matrix
            self.rows = len(matrix)
            self.columns = len(matrix[0])    
    # 

    def __str__(self) -> str:
        re=""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                re+=str(self.matrix[i][j])+ " "
            re+="\n"

        return re

    def multiplication(self, matrix: Matrix):
        # Wenn die anzahl der Spalten der ersten Matrize nicht mit der anzahl der reihen der zweiten übereinstimmen, ist die Multiplikation nicht möglich.

        if self.columns != matrix.rows:
            pass
        else:
            re=[]
            for i in range(0,matrix.columns):
                temp2 = []
                for j in range(0,matrix.columns):
                    temp = 0
                    for k in range(0,matrix.rows):

                        temp += self.matrix[i][k] * matrix.matrix[k][j]
                    
                    temp2.append(temp)
                    
                re.append(temp2)

            return re


    def addition(self,matrix:Matrix):
        # Beide Matrizen brauchen die gleichen dimensionen
        if len(self.matrix)!= len(matrix) or len(self.matrix[0]!= matrix[0]):
            pass
        else:
            re = []
            for i in range(0,len(self.matrix)):
                temp = []
                for j in range(0,len(self.matrix[0])):
                    temp.append( self.matrix[i][j] + matrix.matrix[i][j])
                
                re.append(temp)
            return re
        

    def getDimensions(self) -> list:
        re = []
        re.append(self.columns)
        re.append(self.rows)
        return re
    
    def sobel_operation(self, sobeloperator_x:Matrix,sobeloperator_y:Matrix ):
        re = []
        temp_x =0
        temp_y=0
        for i in range(1,self.rows-1):
            list = []
            for j in range(1,self.columns-1):
                temp_x = self.matrix[i-1][j-1]*sobeloperator_x.matrix[0][0]+self.matrix[i-1][j]*sobeloperator_x.matrix[0][1]+self.matrix[i-1][j+1]*sobeloperator_x.matrix[0][2]+self.matrix[i][j-1]*sobeloperator_x.matrix[1][0]+self.matrix[i][j+1]*sobeloperator_x.matrix[1][2]+self.matrix[i+1][j-1]*sobeloperator_x.matrix[2][0]+self.matrix[i+1][j]*sobeloperator_x.matrix[2][1]+self.matrix[i+1][j+1]*sobeloperator_x.matrix[2][2]

                temp_y = self.matrix[i-1][j-1]*sobeloperator_y.matrix[0][0]+self.matrix[i-1][j]*sobeloperator_y.matrix[0][1]+self.matrix[i-1][j+1]*sobeloperator_y.matrix[0][2]+self.matrix[i][j-1]*sobeloperator_y.matrix[1][0]+self.matrix[i][j+1]*sobeloperator_y.matrix[1][2]+self.matrix[i+1][j-1]*sobeloperator_y.matrix[2][0]+self.matrix[i+1][j]*sobeloperator_y.matrix[2][1]+self.matrix[i+1][j+1]*sobeloperator_y.matrix[2][2]

                list.append(int((temp_y**2+temp_x**2)**0.5))

            re.append(list)

        return re

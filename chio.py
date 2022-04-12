from typing import Tuple, List

class Matrix:
    def __init__(self, x, param=0):
        if isinstance(x, Tuple):
            self.rows = x[0]
            self.cols = x[1]
            self.__matrix = [[param] * self.cols for i in range(self.rows)]
        else:
            self.rows = len(x)
            self.cols = len(x[0])
            self.__matrix = x

    def __getitem__(self, item):
        return self.__matrix[item]

    def __add__(self, other):
        rows2=[]
        cols2=[]
        if self.size()==other.size():
            for i in range(int(self.rows)):
                rows2=[]
                rows2=[self.__matrix[i][j]+other.__matrix[i][j] for j in range(int(self.cols))]
                cols2.append(rows2)
            return Matrix(cols2)

    def __mul__(self, other):

        rows3=[]
        cols3=[]
        if self.rows==other.cols and self.cols==other.rows:
            for i in range(int(self.rows)):
                rows3=[]
                for j in range(int(other.cols)):
                    val=0
                    for k in range(int(self.cols)):
                        val+=self.__matrix[i][k]*other.__matrix[k][j]
                    rows3.append(val)
                cols3.append(rows3)
            return Matrix(cols3)

    def size(self):
        return (self.rows, self. cols)

    def __str__(self):
        string=""
        for i in range(int(self.rows)):
            for j in range(int(self.cols)):
                string+=str(self.__matrix[i][j])+" "
            string+="\n"
        return string

    def chio(self):

        dim = int(self.rows)

        if int(self.rows)==int(self.cols) or dim>=1:

            matrix2=self.__matrix
            multiplier = 1

            if matrix2[0][0]==0:

                for i in range(1,dim):
                    if matrix2[i][0]!=0:
                        pom=matrix2[i][0]

                for i in range(dim):
                    temp_array = matrix2[i][0]
                    matrix2[i][0] = matrix2[i][pom]
                    matrix2[i][pom] = temp_array

                multiplier=multiplier*(-1)


            while dim>=1:
                multiplier=multiplier/(matrix2[0][0])**(dim-2)
                dim=dim-1
                matrix_pom=Matrix((dim, dim))
                for i in range(dim):
                    for j in range(dim):
                        matrix_pom[i][j]=(matrix2[0][0]*matrix2[i+1][j+1]-matrix2[i+1][0]*matrix2[0][j+1])
                matrix2=matrix_pom

            return multiplier





def main():

    matrix1 = Matrix([

    [5 , 1 , 1 , 2 , 3],

    [4 , 2 , 1 , 7 , 3],

    [2 , 1 , 2 , 4 , 7],

    [9 , 1 , 0 , 7 , 0],

    [1 , 4 , 7 , 2 , 2]

    ])


    matrix_2=Matrix([
         [0 , 1 , 1 , 2 , 3],
         [4 , 2 , 1 , 7 , 3],
         [2 , 1 , 2 , 4 , 7],
         [9 , 1 , 0 , 7 , 0],
         [1 , 4 , 7 , 2 , 2]
        ])

    print(matrix1)
    print(matrix1.chio())

    print(matrix_2)
    print(matrix_2.chio())


if __name__ == "__main__":
    main()
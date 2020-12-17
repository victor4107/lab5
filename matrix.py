import copy
import unittest as ut

A = [[1,8,7],
     [5,7,9],
     [6,4,3]]
B = [[1,2,4],
     [9,2,9],
     [5,4,4]]

        
#Вивід заданих матриць

print('Введені матриці: \n')
print('Матриця А: ',A)

print('Матриця В: ',B)



def aaa(A):
    return A

def minor( A, i, j ):
    M = copy.deepcopy(A)
    del M[ i ]
    for i in range( len( A[0] ) - 1 ):
        del M[ i ] [ j ]
    return M   

def det( A ):
    m = len(A)
    n = len(A[0])
    if m != n:
        return None
    if n == 1:
        return A[0][0]
    signum = 1
    determinant = 0
    
    for j in range(n):
        determinant += A[0][j]*signum*det(minor(A, 0, j))
        signum *= -1
    return determinant


    
                     
def matmult(A,B):
    r=[]
    m=[]
    for i in range(len(A)):
        for j in range(len(B[0])):
            sums=0
            for k in range(len(B)):
                sums=sums+(A[i][k]*B[k][j])
            r.append(sums)
        m.append(r)
        r=[]
        
    for i in range(len(m)):
        print(m[i])
    return m

def transp(A):
    for i in range(0,3):
        for j in range(i):
            A[i][j],A[j][i]=A[j][i],A[i][j]
    for i in range(0,3):
        print(A[i])

def sum1(A,B):
    SUM = []
    for i in range(len(A)):
        
        SUM.append([])
        for j in range(len(A[0])):
            SUM[i] += [int(A[i][j] + B[i][j])]
    for i in range(len(SUM)):
        print(SUM[i])

        
def rez(A,B):
    REZ = []
    for i in range(len(A)):
        REZ.append([])
        for j in range(len(A[0])):
            REZ[i] += [int(A[i][j] - B[i][j])]
    for i in range(len(REZ)):
        print(REZ[i])

print('Множення матриць: ')
matmult(A,B)
print('Дискримінант матриці А: ')
print(det(A))
print('Траспонована матриця А:')
transp(A)
print('Сума матриць: ')
sum1(A,B)
print( "Різниця матриць: " )
rez(A,B)
print( "\n" )
print('Результати тестування:')






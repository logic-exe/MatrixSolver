from sympy import *
f = open("Input.txt", "r")
rows=int(f.readline().strip()[-1])
columns=int(f.readline().strip()[-1])
if rows==0 and columns==0:
    print('The entered case is invalid')
    exit()
a=f.readline()
free_var=[]
lhs=''
for i in range(columns):
    free_var.append(i)
    if i==0:
        lhs+=('['+'x'+str(i)+', ')
    elif 0<i<=(columns-2):
        lhs+=('x'+str(i)+', ')
    elif i==(columns-1):
        lhs+=('x'+str(i)+']')
l=[]
for i in range(rows):
    l.append(list(map(float, f.readline().split())))
matrix=Matrix(l)
rref_matrix=matrix.rref()[0]
p_columns=list(matrix.rref()[1])
for i in free_var[:]:
        if i in p_columns:
            free_var.remove(i)
matrix=eval(str(rref_matrix)[7:-1])
print('RREF of the given matrix is ↓')
for i in matrix:
    print(i)

print()
print()
print('Parametric form of the given matrix is ↓')
print('x =',lhs,'=',end=' ')

for i in free_var:
    vector=[]
    for j in range(rows):
        vector.append(-1*matrix[j][i])
    for k in range(columns-rows):
        vector.append(0)
    vector[i]=1
    print(str(vector)+'*x'+str(i),end=' + ')
print([0]*columns)


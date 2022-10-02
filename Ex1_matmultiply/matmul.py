import random
import numpy as np

matrix1 = np.random.randint(3, size=(3,3))
matrix2 = np.random.randint(3, size=(3,3))
matrix4 = np.zeros((3,3))
rows = 3
columns = 3
matrix3 = [[random.randrange(0, 10) for x in range(columns)] for y in range(rows)]

for x in range(columns):
	for y in range(rows):
		matrix4[x][y] = random.randrange(0,10)

print("------ Z -----")
print(matrix4)

print(matrix3)

print(matrix3[2][0])
print("-------------")

print("----  X  -----")
print(matrix1)
print("----  Y  -----")
print(matrix2)
print("-------------!")
result = np.zeros((3,3))

for i in range(len(matrix1)):
   # iterate through columns of Y
   for j in range(len(matrix2[0])):
       # iterate through rows of Y
       for k in range(len(matrix2)):
           result[i][j] += matrix1[i][k] * matrix2[k][j]

for r in result:
   print(r)
print("------------")
print(result)

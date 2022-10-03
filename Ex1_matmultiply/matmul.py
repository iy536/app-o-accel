import random
import numpy as np

''' Implementation without numpy library'''
rows = 3
columns = 3
matrix1 = [[0,0,0],
           [0,0,0],
           [0,0,0]]
matrix2 = [[0,0,0],
           [0,0,0],
           [0,0,0]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
result2 = [[0,0,0],
          [0,0,0],
          [0,0,0]]


for x in range(columns):
	for y in range(rows):
		matrix1[x][y] = random.randrange(0,10); matrix2[x][y] = random.randrange(0,10)

# Matrix multiplication has been performed in following for-loop

for i in range(len(matrix1)):
      # iterate through columns of matrix2
      for j in range(len(matrix2[0])):
        # iterate through rows of matrix2
        for k in range(len(matrix2)):
           result[i][j] += matrix1[i][k] * matrix2[k][j]
print(matrix1)
print(matrix2)
print(result)



# matmul() function performs Matrix Multiplication

def matmul(rows,columns):
   for x in range(columns):
	   for y in range(rows):
		   matrix1[x][y] = random.randrange(0,10); matrix2[x][y] = random.randrange(0,10)
   
   for i in range(len(matrix1)):
      # iterate through columns of matrix2
      for j in range(len(matrix2[0])):
        # iterate through rows of matrix2
        for k in range(len(matrix2)):
           result2[i][j] += matrix1[i][k] * matrix2[k][j]
           return print(result)

print("Function call")
print(matrix1)
print(matrix2)
matmul(3,3)
print("--------------")


''' Implementation with numpy library
    Let's initialize 3x3 matrices with
    random integers range 0 to 9
'''

matrix1 = np.random.randint(10, size=(3,4))
matrix2 = np.random.randint(10, size=(4,3))
result = np.zeros((3,3))


print("--------matrixes with numpy------")
print(matrix1)
print(matrix2)

for i in range(len(matrix1)):
   # iterate through columns of matrix2
   for j in range(len(matrix2[0])):
       # iterate through rows of matrix2
       for k in range(len(matrix2)):
           result[i][j] += matrix1[i][k] * matrix2[k][j]

for r in result:
   print(r)
# print("------------")
print(result)

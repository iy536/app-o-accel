import random
import numpy as np


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


# matmul() function performs Matrix Multiplication

   
def matmul(row,columns):
   # Lets fill matrix1 and matrix2 with random integers of range 0-9.
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
   print("---- matrix1 ----")
   for m1 in matrix1:
      print(m1)
   print("---- matrix2 ----")
   for m2 in matrix1:
      print(m2)
   print("---- result ----")
   for r in result:
      print(r)
   return result

#Function call   
matmul(3,3)




#####################################
# Implementation with numpy library #
#####################################

def matmulnp(rows,columns):
   #Let's initialize 3x3 matrices with random integers of range 0 to 9
   matrix1 = np.random.randint(10, size=(3,3))
   matrix2 = np.random.randint(10, size=(3,3))
   result = np.zeros((3,3))
   
   for i in range(len(matrix1)):
   # iterate through columns of matrix2
      for j in range(len(matrix2[0])):
         # iterate through rows of matrix2
         for k in range(len(matrix2)):
           result[i][j] += matrix1[i][k] * matrix2[k][j]
   print("\n  Implementation with numpy library")
   print("---- matrix1 ----")
   print(matrix1)
   print("---- matrix2 ----")
   print(matrix2)
   print("---- result ----")
   return print(result)

#Function call
matmulnp(3,3)

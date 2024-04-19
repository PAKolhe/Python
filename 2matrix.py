def mul_matrices(mat1, mat2):
 result = [[mat1[i][j] * mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
 return result
# Input matrices
matrix1 = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
matrix2 = [[9, 8, 7],
[6, 5, 4],
[3, 2, 1]]
# Add matrices
result = mul_matrices(matrix1, matrix2)
# Display matrices and their sum
print("Matrix 1:")
for row in matrix1:
 for elem in row:
  print(elem, end=" ")
print()
print("\nMatrix 2:")
for row in matrix2:
 for elem in row:
  print(elem, end=" ")
print()
print("\nMatrix Multiplication:")
for row in result:
 for elem in row:
  print(elem, end=" ")
print()

pragati pragati pragati
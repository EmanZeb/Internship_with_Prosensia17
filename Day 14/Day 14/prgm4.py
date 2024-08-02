class MatrixDimensionMismatchError(Exception):
    pass

class NonNumericValueError(Exception):
    pass

def add_matrices(matrix1, matrix2):    #Func

  if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
    raise MatrixDimensionMismatchError("Matrices must have the same dimensions")

  for row1, row2 in zip(matrix1, matrix2):
    for num1, num2 in zip(row1, row2):
      if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise NonNumericValueError("Matrices must contain only numbers")

  result = [[num1 + num2 for num1, num2 in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]
  return result

# Exmp used
matrix1 = [[2, 4], [6, 8]]
matrix2 = [[1, 3], [5, 7]]
try:
  result_matrix = add_matrices(matrix1, matrix2)
  print(result_matrix)
except (MatrixDimensionMismatchError, NonNumericValueError) as e:
  print(e)
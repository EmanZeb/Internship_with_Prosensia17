import cmath         #Call library

def complex_number_operations(complex_str, other_complex):   #func
   complex_num = complex(complex_str)

  addition = complex_num + other_complex
  subtraction = complex_num - other_complex
  multiplication = complex_num * other_complex
  division = complex_num / other_complex

  return addition, subtraction, multiplication, division

# Exmp used 
complex_str = '2+3j'
other_complex = 4 - 2j
results = complex_number_operations(complex_str, other_complex)
print(results)
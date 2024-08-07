import math      #Call lib

def prime_factors(num):      #Func

  if num <= 1:
    return [], 1

  factors = []
  product = 1
  while num % 2 == 0:
    factors.append(2)
    product *= 2
    num //= 2

  for i in range(3, int(math.sqrt(num)) + 1, 2):
    while num % i == 0:
      factors.append(i)
      product *= i
      num //= i

  if num > 1:
    factors.append(num)
    product *= num

  return factors, product

# Exmp used
number = 25
factors, product = prime_factors(number)
print(factors)  
print(product)  
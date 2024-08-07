import statistics       #lib

def normalize_and_stats(numbers):     #func

  if not numbers:
    raise ValueError("List cannot be empty")

  if not all(isinstance(num, (int, float)) for num in numbers):
    raise ValueError("List contains non-numeric values")

  min_value = min(numbers)
  max_value = max(numbers)
  range_value = max_value - min_value

  normalized_numbers = [(num - min_value) / range_value for num in numbers]

  mean = statistics.mean(normalized_numbers)
  median = statistics.median(normalized_numbers)
  variance = statistics.variance(normalized_numbers)

  return normalized_numbers, mean, median, variance

# Exmp used
numbers = [1, 2, 3, 4, 5]
normalized_data, mean, median, variance = normalize_and_stats(numbers)
print(normalized_data)
print(mean)
print(median)
print(variance)
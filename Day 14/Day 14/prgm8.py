def flatten_list(nested_list):   

  def flatten_helper(nested_list, depth):
    flattened = []
    for item in nested_list:
      if isinstance(item, list):
        flattened.extend(flatten_helper(item, depth + 1))
      else:
        flattened.append(item)
    return flattened, depth

  flattened_list, depth = flatten_helper(nested_list, 0)
  return flattened_list, depth + 1

# Exmp used
nested_list = [1, [2, [3, 4]], 5, [6, 7]]
flattened, depth = flatten_list(nested_list)
print(flattened)  
print(depth)  
def reverse_string(string):

  return string[::-1]

def main():
  input_string = input("Enter a string: ")
  reversed_string = reverse_string(input_string)
  print("Reversed string:", reversed_string)

if _name_ == "_main_":
  main()
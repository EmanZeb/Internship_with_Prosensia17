import json
import logging      #Calling libraries

def dict_to_json_and_back(data):    #Func

  error_message = None
  try:
    json_string = json.dumps(data)
    dict_back = json.loads(json_string)
  except (TypeError, ValueError) as e:
    json_string = None
    dict_back = None
    error_message = f"Error converting dictionary to JSON: {e}"
    logging.error(error_message)

  return json_string, dict_back, error_message

# Exmp used
data = {'name': 'Eman', 'age': 19, 'city': 'Haripur'}
json_str, dict_back, error = dict_to_json_and_back(data)

if error:
  print(error)
else:
  print(json_str)
  print(dict_back)
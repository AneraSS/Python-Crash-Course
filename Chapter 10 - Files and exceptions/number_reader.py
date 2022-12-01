import json

filename ='numbers.json' # we've created the file with number_writer
with open(filename) as f:
    numbers = json.load(f)

print(numbers)
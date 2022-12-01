# STORING DATA
# using json module

# json.dump() - stores - takes 2 arguments: (1) piece data to store and (2) file object it can use zo store the data
# json.load() - reads data back into memory

import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json' # not yet previously created
with open(filename, 'w') as f:
    json.dump(numbers,f)


numbers = []
for number in range (1,11):
    numbers.append(number**3) #cube
print(numbers)

#use a list comprehension
numbers = [number**3 for number in range (1,11)]
print (numbers)
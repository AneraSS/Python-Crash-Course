print ("--- the while loop in action --- ")

current_number = 1

while current_number <=5:
    print (current_number)
    current_number +=1 # same as current_number = current_number +1

print ("--- letting the user choose when to quit --- ")

prompt = input ("How long should I count before I quit counting?: ")
prompt = int(prompt)

summa=0

for current_number in range(0, prompt+1):
    summa += current_number
    print (summa)


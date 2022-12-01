print ("-- using int() to accept numerical input --")

question = "How old are you? "
age = input (question)
if int(age) < 18:
    print ("You're too young to vote.")
else:
    print ("You can vote!")

# he expected string and int(x) converts it to integer


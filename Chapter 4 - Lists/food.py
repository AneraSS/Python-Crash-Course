my_foods = ["burger", "McDonalds", "sushi", "raw tuna", "ice cream", "salad"]
his_foods = my_foods[:] #we have an exact the same list
print (f"My favourite food are: {sorted(my_foods)}")
print ("Martin likes:", his_foods)

my_foods.append("kinder pingui")
his_foods.append("kinder milchschnitte")
print("My list:", my_foods)
print("Martin's list:", his_foods)

my_foods.insert(2, "cherry")
his_foods.insert(3, "avocado")
print("My list:", my_foods)
print("Martin's list:", his_foods)

print("\nMy list:")
for food in my_foods:
    print ("\t", food)

print("\nMartin's list:")
for food in his_foods:
    print (f"\t{food}") #sad nema space

    
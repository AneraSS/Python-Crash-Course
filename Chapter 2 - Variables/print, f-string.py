#page 15
print ("Od danas krecem uciti ponovnoo Phyton")

# page 16
message ="Martin je ful naporan kada mi pametuje, ali se trudi"
print (message)
message2 = "ovo  je sada dodatna poruka"
print (message2)

# page 20, changing case in a string with methods
name = "anera svarc sosic"
print (name.title()) #svaka rijec zapocinje velikim slovom
print (name.upper()) #velika tiskana
print (name.lower()) #mala tiskana

# page 21, using the f-string
first_name = "martin"
last_name = "sosic"
full_name = f"{first_name} {last_name}" #izmedu viticastih je razmak
print(full_name.title())
print ("Moj", full_name.title(), "je najbolji muz na svijetu!")
print (f"Doduse {name.title()} je najbolja zena na svijetu!")
couple = f"{first_name.title()} i {name.title()} su najbolji supruznici ikada!"
print (couple)

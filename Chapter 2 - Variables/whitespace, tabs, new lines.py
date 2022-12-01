#page 22
# whitespace: .lstrip() .rstrip()
# novi red \n
# novi tab \t
print ("pas:")
print ("\tRiu") #dodaje tab
print ("Lucky", "\nHollie") # novi red
print ("\nmace:", "\n\tTina", "\n\tKira") # prvo ide novi red, pa novi tab
print ("Zivotinje su:\n\tpsi\n\tmace")
favourite = " Whippet "
print (f"{favourite}")
print (favourite)
print (favourite.rstrip()) #uklanja desni razmak (whitespace) .rstrip()
favourite = favourite.rstrip() #trajno uklanjanje desnog razmaka
print (favourite)
print (favourite.lstrip()) #uklanja lijevi razmak .lstrip()
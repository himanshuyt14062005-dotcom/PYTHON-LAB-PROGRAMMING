fruits = []
for i in range(5):
    fruit = input("enter fruit:")
    
    fruits.append(fruit) # add krne k leye

print("original fruits list:",fruits)

old = input("enter old fruit:")  # fruits list hogi jo riplace krna 
new = input("enter new fruit:")  # replace krne k bad new list hogi

for i in range(5):
    if fruits[i] == old:
        fruits[i] = new
        print("update list:",fruits)        
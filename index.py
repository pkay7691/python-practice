# index operator [] = gives access to a sequences element

name = "bro Code!"

if(name[0].islower()): 
    name = name.capitalize()


first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]
print(name)
print(first_name)
print(last_name)
print(last_character)


people = 20
cats = 30
dogs = 15

if people < cats:                                        #20 < 30
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:                                       #20 < 30
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:                                     #30 = 30
    print("people are dogs.")


# PS C:\Users\miran\lpthw>  python ex29.py
# Too many cats! The world is doomed!
# The world is dry!
# People are greater than or equal to dogs.
# People are less than or equal to dogs.
# people are dogs.

#1. x += 1  x = x + 1

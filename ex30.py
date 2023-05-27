people = 30
cars = 40
trucks = 15
# > < =     if elif else:
if cars > people:                           #40>30
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
#> < =
if trucks > cars:
    print("Tha's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.") #15<40
else:
    print("We still can't decide.")
#> <=
if people > trucks:                          #30>15
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

# PS C:\Users\miran\lpthw> python ex30.py
# We should take the cars.
# Maybe we could take the trucks.
# Alright, let's just take the trucks.

#Python只会运行它遇到的是True的第一个块，所以只有第一个为True的块运行。

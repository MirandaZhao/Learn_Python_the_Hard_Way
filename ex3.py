# ex3
print('I will now count my chickens:')

print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)  # first * then % last -

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it True that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)  # False

print("What is 3 + 2?", 3 + 2)  # What is 3 + 2? 5

print("What is 5 - 7?", 5 - 7)  # What is 5 - 7? -2

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)  # True

print("Is it greater or equal?", 5 >= -2)  # True

print("Is it less or equal?", 5 <= -2)  # False


#1. remove comma after hens return error:
#   File "C:\Users\miran\lpthw\ex3.py", line 4
#     print("Hens" 25 + 30 / 6)
#           ^^^^^^^^^^^^^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# PS C:\Users\miran\lpthw>

#2.remove * between roosters return error:
# PS C:\Users\miran\lpthw> python .\ex3.py
#   File "C:\Users\miran\lpthw\ex3.py", line 5
#     print("Roosters", 100 - 25  3 % 4)  # first * then % last -
#                       ^^^^^^^^^^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?

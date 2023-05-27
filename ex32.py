#循环和列表

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"This is count{number}")

for fruit in fruits:
    print(f"A ruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

elements = []
for i in range(0,6):
    print(f"Adding {i} to the list.")                                           #输入前打印
    elements.append(i)
    print(elements)                                                             #输入后打印

for i in elements:
    print(f"Element was: {i}")

# PS C:\Users\miran\lpthw> python 32.py
# C:\Users\miran\AppData\Local\Programs\Python\Python311\python.exe: can't open file 'C:\\Users\\miran\\lpthw\\32.py': [Errno 2] No such file or directory
# PS C:\Users\miran\lpthw> python ex32.py
# This is count1
# This is count2
# This is count3
# This is count4
# This is count5
# A ruit of type: apples
# A ruit of type: oranges
# A ruit of type: pears
# A ruit of type: apricots
# I got 1
# I got pennies
# I got 2
# I got dimes
# I got 3
# I got quarters
# Adding 0 to the list.
# [0]
# Adding 1 to the list.
# [0, 1]
# Adding 2 to the list.
# [0, 1, 2]
# Adding 3 to the list.
# [0, 1, 2, 3]
# Adding 4 to the list.
# [0, 1, 2, 3, 4]
# Adding 5 to the list.
# [0, 1, 2, 3, 4, 5]
# Element was: 0
# Element was: 1
# Element was: 2
# Element was: 3
# Element was: 4
# Element was: 5

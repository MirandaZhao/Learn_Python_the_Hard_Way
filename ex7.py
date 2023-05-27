# ex7
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))  # Its fleece was white as snow.
print(f"Its fleece was white as {'snow'}.")  # Its fleece was white as snow.
print("Its fleece was white as {}.".format())
print("And everywhere that Mary went.")
print("." * 10)  # ..........

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6, end='')  # CheeseBurger
#print(end1 + end2 + end3 + end4 + end5 + end6)
#Cheese
#Burger
#print(end1 + end2 + end3 + end4 + end5 + end6, end=':')  # Cheese:Burger
#print(end1 + end2 + end3 + end4 + end5 + end6, end='  ')  # Cheese Burger
print(end7 + end8 + end9 + end10 + end11 + end12)

#1.format: string+format: {}.format = f

#2.if not need a new line, using end=''
#eg. print(end1 + end2 + end3 + end4 + end5 + end6) will return 2 lines result in stead of 1

#3.change line 21 to print(end1 + end2 + end3 + end4 + end5 + end6, end=':')
#returns Cheese:Burger

#4.change line 21 to print(end1 + end2 + end3 + end4 + end5 + end6, end='  ') 2 spaces inside
#returns Cheese Burger

#5.remove * in line 6 returns error:
#   File "C:\Users\miran\lpthw\ex7.py", line 7
#     print("."  10)
#           ^^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?

#6. if remove snow in line 3 returns "Its fleece was white as ."

#7. if remove snoe in line 3 as print("Its fleece was white as {}.".format())
#returns erros:
# Traceback (most recent call last):
#   File "C:\Users\miran\lpthw\ex7.py", line 5, in <module>
#     print("Its fleece was white as {}.".format())
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# IndexError: Replacement index 0 out of range for positional args tuple

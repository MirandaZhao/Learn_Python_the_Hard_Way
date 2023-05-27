# ex5
# f means format
my_name = 'Zed A. Shaw'
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

#1.In powershell, typing clear will clear all things up

#2.delete line 11 "f" return :Let's talk about {my_name}.

#3. delete line 11 "}" return:Let's talk about {my_name.

#4. change line 11 {my_name} to {name} return: Let's talk about {name}.

#5. change line 18 " my_height" to "height" returns error:
# Traceback (most recent call last):
#   File "C:\Users\miran\lpthw\ex5.py", line 18, in <module>
#     total = my_age + height + my_weight
#                      ^^^^^^
# NameError: name 'height' is not defined. Did you mean: 'my_height'?

#6. change line 12 from "my_height" to "my_height + my_weight"
#returns result from 74 to 254
#==> can combine things together in f

#7. change line 12 from "{my_height}" to {print("This.")}
# returns error:
#   File "C:\Users\miran\lpthw\ex5.py", line 13
#     print(f"He's {print("This.")} inches tall.")
#                          ^^^^
# SyntaxError: f-string: unmatched '('
# ==> can't put print inside the f

#8. change line 12 from "{my_height}" to "{my_age + my_eyes}"returns error:
# Traceback (most recent call last):
#   File "C:\Users\miran\lpthw\ex5.py", line 13, in <module>
#     print(f"He's {my_age + my_eyes} inches tall.")
#                   ~~~~~~~^~~~~~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ==> cant put int and str together!

#9. change line 12 from "{my_height}" to f"Hi {my_eyes}" returns error:
# PS C:\Users\miran\lpthw> python ex5.py
#   File "C:\Users\miran\lpthw\ex5.py", line 13
#     print(f"He's {f"Hi {my_eyes} inches tall.")
#                                              ^
# SyntaxError: unterminated string literal (detected at line 13)
# ==> cant put f string inside the f string

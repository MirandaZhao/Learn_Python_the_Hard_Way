#ex11:
print("How old are you?", end = '')
age = input()
#age = int(input())
print(">>>age=" , repr(age))
print("How tall are you?", end = '')
height = input()
print("How much do you weight?", end = '')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight}  heavy.")


# PS C:\Users\miran\lpthw> python ex11.py
# How old are you?42
# How tall are you?6'2"
# How much do you weight?190lbs
# So, you're 42 old, 6'2" tall and 190lbs  heavy.

#1. if change line 3 to age = int(input())
#then I could not input string like asdfk to Q1 how old are you
#it will return error as
# Traceback (most recent call last):
#   File "C:\Users\miran\lpthw\ex11.py", line 4, in <module>
#     age = int(input())
#           ^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'asdfk'

#2. if change line 3 and line 4 to
# age = int(input())
# print(">>>age=" , repr(age))
# when I type asdfk to Q1 how old are you
# it will return
# How old are you?asdfk
# >>>age= 'asdfk'                           ==> quote will tell data type!!!
# How tall are you?sadfl
# How much do you weight?dlfa
# So, you're asdfk old, sadfl tall and dlfa  heavy.

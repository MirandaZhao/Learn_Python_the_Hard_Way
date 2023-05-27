from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("The first variable is:", first)
print("The second variable is:", second)
print("The third variable is:", third)

# 输入指令：PS C:\Users\miran\lpthw> python ex13.py first 2nd 3rd
# The script is called: ex13.py
# The first variable is: first
# The second variable is: 2nd
# The third variable is: 3rd

#PS C:\Users\miran\lpthw> python ex13.py stuff things that
# The script is called: ex13.py
# The first variable is: stuff
# The second variable is: things
# The third variable is: that

# PS C:\Users\miran\lpthw>  python ex13.py apple orange grapefruit
# The script is called: ex13.py
# The first variable is: apple
# The second variable is: orange
# The third variable is: grapefruit

#只输入两个变量会报错
# PS C:\Users\miran\lpthw> python ex13.py first 2nd
# Traceback (most recent call last):
#   File "C:\Users\miran\lpthw\ex13.py", line 3, in <module>
#     script, first, second, third = argv
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: not enough values to unpack (expected 4, got 3)

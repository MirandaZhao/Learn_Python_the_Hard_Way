# ex8
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))  # 1 2 3 4
print(formatter.format("one", "two", "three", "four"))  # one two three four
print(formatter.format(True, False, False, True))  # True False False True
print(formatter.format(formatter, formatter, formatter, formatter))  # {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))  # Try your Own text here Maybe a poem Or a song about fear


#learn debug method 1:
# adding lines:
# lines = (
#     "Try your"
#     "Own text here",
#     "Maybe a poem",
#     "Or a song about fear"
# )
# print(">>lines", repr(lines))
# print(formatter.format(*lines))

#learn debug method 2:
# print(">>>"
#     "Try your"
#     "Own text here",
#     "Maybe a poem",
#     "Or a song about fear"
# )
# print(formatter.format(
#     "Try your"
#     "Own text here",
#     "Maybe a poem",
#     "Or a song about fear"
# ))


# 1. formatter.format(...) --> 取fomatter字符串，.format表示调用函数:执行一个叫format的命令行，给format传递4个参数:将参数传递给format命令，

# 2. 在formmatter上调用format的结果是一个新字符串，其中{}被4个变量替换掉了，这就是print打印结果。

# 3. if remove . in line 5 as print(formatterformat(1, 2, 3, 4))
# returns error:
# Traceback (most recent call last):
#   File "C:\Users\miran\lpthw\ex8.py", line 5, in <module>
#     print(formatterformat(1, 2, 3, 4))  # 1 2 3 4
#           ^^^^^^^^^^^^^^^
# NameError: name 'formatterformat' is not defined

# 4. remove { in line 2 as formatter = "} {} {} {}"
#returns error:
# Traceback (most recent call last):
#   File "C:\Users\miran\lpthw\ex8.py", line 4, in <module>
#     print(formatter.format(1, 2, 3, 4))  # 1 2 3 4
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: Single '}' encountered in format stri

#5. remove {} in line 2 as formatter = " {} {} {}"
# returns less values than before ==> python eat up the final argument
 # 1 2 3
 # one two three
 # True False False
 #  {} {} {}  {} {} {}  {} {} {}
 # Try your Own text here Maybe a poem

 #6. remove ) in line 4 as print(formatter.format(1, 2, 3, 4)
 #returns error:
#  File "C:\Users\miran\lpthw\ex8.py", line 4
#     print(formatter.format(1, 2, 3, 4)  # 1 2 3 4
#          ^
# SyntaxError: '(' was never closed

#7. remove the " in line 2 returns as formatter = "{} {} {} {}
# returns error as
# File "C:\Users\miran\lpthw\ex8.py", line 2
#     formatter = "{} {} {} {}
#                 ^
# SyntaxError: unterminated string literal (detected at line 2)

#8 change False to false in line 6
#return
# Traceback (most recent call last):
#   File "C:\Users\miran\lpthw\ex8.py", line 6, in <module>
#     print(formatter.format(True, false, False, True))  # True False False True
#                                  ^^^^^
# NameError: name 'false' is not defined. Did you mean: 'False'?

#9 remove comma in line 9 as "Try your" returns error as
#Traceback (most recent call last):
#   File "C:\Users\miran\lpthw\ex8.py", line 8, in <module>
#     print(formatter.format(
#           ^^^^^^^^^^^^^^^^^
# IndexError: Replacement index 3 out of range for positional args tuple #索引错误

#10.1 adding lines debug method1 shows the error as
# Traceback (most recent call last):
#   File "C:\Users\miran\lpthw\ex8.py", line 33, in <module>
#     print(formatter.format(*lines))
#           ^^^^^^^^^^^^^^^^^^^^^^^^
# IndexError: Replacement index 3 out of range for positional args tuple

#10.2 print debug method 2 shows the error as
# Traceback (most recent call last):
#   File "C:\Users\miran\lpthw\ex8.py", line 42, in <module>
#     print(formatter.format(
#           ^^^^^^^^^^^^^^^^^
# IndexError: Replacement index 3 out of range for positional args tuple

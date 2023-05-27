from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input(">")

text_again = open(file_again)

print(text_again.read())


# PS C:\Users\miran\lpthw> python ex15.py ex15_sample.txt
# Here's your file ex15_sample.txt:
# This is stuff I typed into a file
# It is really cool stuff.
# Lots and lots of fun to have in here.
#
# Type the filename again:
# >ex15_sample.txt
# This is stuff I typed into a file
# It is really cool stuff.
# Lots and lots of fun to have in here.

#line1-3:使用argv获取文件名，line 5使用open命令
#line 7: txt调用read函数，从open获得的东西是一个file文件，接受命令的方式使用句点.方式紧跟着命令名，再跟这类似open和input的参数。
#txt.read时，意思是执行read命令，无需任何参数

#那种open方式更好？

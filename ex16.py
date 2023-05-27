from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w') #w:write


print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()                                      #如忘记关文件，会leak文件


# PS C:\Users\miran\lpthw> python ex16.py ex16_sample.txt
# We're going to erase ex16_sample.txt.
# If you don't want that, hit CTRL-C (^C).
# If you do want that, hit RETURN.
# ?
# Opening the file...
# Truncating the file. Goodbye!
# Now I'm going to ask you for three lines.
# line 1:Mary had a little lamb
# line 2:It's fleece was white as snow
# line 3:It was also tasty
# I'm going to write these to the file.
# And finally, we close it.

#program是去移除原来文本中的内容，再写入新的内容。
#？hit ctrl C好像没有作用
#在输入指令时，如果有空格可能影响输出结果
#'w'是特殊字符串，代表写入(write)，'r'表示读取(read)，'a'表示追加append.
#用+修饰符：来实现'w+','r+','a+'，可以把文件同时读写方法打开，根据使用的字符，以不一样的方式实现文件定位。
#open(filename)，就使用'r'模式打开。

#1)if remove line 12 'w' as target = open(filename)
# returns error:
# Traceback (most recent call last):
#   File "C:\Users\miran\lpthw\ex16.py", line 16, in <module>
#     target.truncate()
# io.UnsupportedOperation: truncate
# PS C:\Users\miran\lpthw>

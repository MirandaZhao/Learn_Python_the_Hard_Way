# ex10
print("I am 6'2\" tall.")  # 将双引号转义 #I am 6'2" tall.
print('I am 6\'2" tall.')  # 将单引号转义 #I am 6'2" tall.

tabby_cat = "\tI'm tabbed in."  # \t 是tab缩进
persian_cat = "I'm split\non a line."  # \n是换行
backslash_cat = "I'm \\ a \\ cat."  # I'm \ a \ cat.

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# I'll do a list:
#	* Cat food
#	* Fishies
#	* Catnip
#	* Grass

# 转义序列escape sequence：

# \\：反斜杠\
# \':单引号'
# \":双引号"
# \n:换行符: new line character
# \r:回车符 carriage return
# \t:制表符

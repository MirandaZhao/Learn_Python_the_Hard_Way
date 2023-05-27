# ex9
#escaping sequence is a way to add lines/tabs in a string without breaking it
# print 句；行；段落
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"  # \n是换行
months1 = "\nJan\nFeb\nMar\"\nApr\nMay\nJun\nJul\nAug"  # \"return "

print("Here are the days:", days)  # Mon Tue Wed Thu Fri Sat Sun
print("Here are the months:", months)
print("Here are the months:", months1)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

#1. if remove one " line 10 returns error:
#   File "C:\Users\miran\lpthw\ex9.py", line 11
#     There's something going on here.
#          ^
# SyntaxError: unterminated string literal (detected at line 11)
# PS C:\Users\miran\lpthw>

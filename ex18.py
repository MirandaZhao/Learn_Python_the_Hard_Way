#function【未视频】
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1:{arg1}, arg2:{arg2}")                   #少过"，报错SyntaxError: unterminated string literal

def print_two_again(arg1, arg2):                         #丢失过_, 报错SyntaxError
    print(f"arg1:{arg1}, arg2:{arg2}")

def print_one(arg1):
    print(f"arg1:{arg1}")

def print_none():
    print("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

# PS C:\Users\miran\lpthw>  python ex18.py
# arg1:Zed, arg2:Shaw
# arg1:Zed, arg2:Shaw
# arg1:First!
# I got nothin'.

#*args里的*：把函数的所有参数都接受进来，然后放到名叫args的列表中，和一直在用的argv差不多。
#argv是用在函数上。没有特殊需要，一般不会用到*。

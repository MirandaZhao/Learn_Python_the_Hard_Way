from sys import argv

script, user_name = argv
prompt = '>'                                              #可以换成任何符号

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

# PS C:\Users\miran\lpthw> python ex14.py Yuchen
# Hi Yuchen, I'm the ex14.py script.
# I'd like to ask you a few questions.
# Do you like me Yuchen?
# >yes
# Where do you live Yuchen?
# >beijing
# What kind of computer do you have?
# >mac pro

#使用argv和input一起向用户提问。用input(prompt)的方式，显示>作为提示符。
#使用prompt, 就不需要每次用input时反复输入提示的字符。？
#如果将提示符修改成别的字符串，只要改一个位置就可以了。？
#当运行脚本是，要把名字附给脚本，让argv参数收到名字。
#prompt = '>' input(prompt) ，区别于input("AAA?")的是在执行时，输入变成另起一行的>符号。
#习得"""与{}结合

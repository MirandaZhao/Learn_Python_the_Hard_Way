from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)   #exit(0)用于正常结束程序并返回状态码，以指示程序是否成功执行。      #exit(0) 是一个函数调用，它的作用是终止当前正在执行的程序并返回一个状态码。在这个函数中，参数0表示程序正常退出，而非因为错误或异常而退出。
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input(">")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input(">")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good Job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input(">")

    if choice == 'left':
        bear_room()
    elif choice == 'right':
        cthulhu_room()
    else:
        dead("You stumble around the room untill you starve.")

start()


# PS C:\Users\miran\lpthw> python ex35.py
# You are in a dark room.
# There is a door to your right and left.
# Which one do you take?
# >left
# There is a bear here.
# The bear has a bunch of honey.
# The fat bear is in front of another door.
# How are you going to move the bear?
# >taunt bear
# The bear has moved from the door.
# You can go through it now.
# >open door
# This room is full of gold. How much do you take?
# >1000
# You greedy bastard! Good Job!

#LOGIC:
#Q1:You are in a dark room.
# There is a door to your right and left.
# Which one do you take?

#1.left -> bear_room
#2.right -> cthulhu_room
#3.XXX -> You stumble around the room untill you starve. Good Job!

#Q2: bear_room:
# There is a bear here.
# The bear has a bunch of honey.
# The fat bear is in front of another door.
# How are you going to move the bear?

#1.take honey: The bear looks at you then slaps your face off.
#2.taunt bear:The bear has moved from the door.
#You can go through it now.
#i. taunt bear: The bear gets pissed off and chews your leg off. Good Job!
#ii. open_door--> Q3:

#Q3:This room is full of gold. How much do you take?
#1.0 or 1: Nice, you're not greedy, you win!
#2.2-49: Man, learn to type a number.
#3.50 +：You greedy bastard! Good job!

#if 语句规则：
#1. 1条语句必须包含一个else
#2. if语句的嵌套不要超过两层，最好尽量保持只有一层
#3. 每一个if, elif, else组合，在这个组合的最前面和最后面留一个空行以作区分
#4. 调试的最好方法，是用print在哥哥想要检查的关键点将变量打印出来
#5. 程序一部分一部分运行起来，不要全写完再运行。

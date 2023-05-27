print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input(">")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input(">")
                                                                                #if语句内部，再放一个if语句作为可运行代码
    if bear == "1":
        print("The bear eats your face off. Good job!")                         #吃脸
    elif bear == "2":
        print("The bear eats your legs off. Good job!")                         #吃腿
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")                                                #跑了

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")              #你在克苏鲁的视网膜上凝视着无尽的深渊
    print("1. Blueberries.")                                                    #1、蓝莓
    print("2. Yellow jacket clothespins.")                                      #2. 黄色夹克衣夹。
    print("3. Understanding revolvers yelling melodies.")                       #3. 理解左轮手枪的喊叫旋律。

    insanity = input(">")                                                       #疯狂

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")                 #你的身体在果冻的帮助下得以生存。
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")               #精神错乱会让你的眼睛变成一滩烂泥。
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")           #你跌跌撞撞摔在刀上死了。干得好！

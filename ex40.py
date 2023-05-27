#1.字典：dictionary['key'] = value
mystuffs = {'apple':"I am the apples!"}
print(mystuffs['apple'])   #I am the apples!


# print('-' * 10)
# #2.模块(module)：在一个mystuff.py中，放一个apple函数。
# #this goes in mystuff.py
# def apple():
#     print("I am the apples!")
#
# print('-' * 10)
# #3.可以用import来调用模块，访问apple函数。
import mystuff
# mystuff.apple()         # I am the apples!
#
# print('-' * 10)
# #4.放一个tangerine的变量到模块里
# import mystuff
#
# mystuff.apple()          #I am the apples!
# print(mystuff.tangerine) #Living reflection of a dream

print('-' * 10)
#5.不同语法访问这个变量
print(mystuffs['apple'])   #I am the apples!
print(mystuff.apple())     #I am the apples!
print(mystuff.tangerine)   #Living reflection of a dream

print('-' * 10)
#6.建立class
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I am classy apples!")

thing = MyStuff()
thing.apple()            #I am classy apples!
print(thing.tangerine)   #And now a thousand years between

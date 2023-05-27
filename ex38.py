ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')                                                   #将string化为list, len(stuff) = 6
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
print(f"print stuff:",stuff)

while len(stuff) != 10:
    next_one = more_stuff.pop()                                                  #pop是拿more_stuff的最后一个element
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go:", stuff)                                                    # ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']

print("Let's do some things with stuff.")

print(stuff[1]) #oranges

print(stuff[-1]) #Corn

print(stuff.pop()) #Corn

print(' '.join(stuff)) #Apples Oranges Crows Telephone Light Sugar Boy Girl Banana     #' '.join(list): 将list中每个element用空格连接

print('&'.join(stuff[3:5])) #Telephone&Light  #[3:5]是取第4和第5个                      #'&'.join(list): 将list中每个element用&连接


# PS C:\Users\miran\lpthw> python ex38.py
# Wait there are not 10 things in that list. Let's fix that.
# print stuff: ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar']
# Adding: Boy
# There are 7 items now.
# Adding: Girl
# There are 8 items now.
# Adding: Banana
# There are 9 items now.
# Adding: Corn
# There are 10 items now.
# There we go: ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
# Let's do some things with stuff.
# Oranges
# Corn
# Corn
# Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
# Telephone&Light


#1.何时使用list: 维持次序；通过一个数字来随机访问内容（从0开始基数访问)；线性从头到尾访问内容
#2.取出每一个被调用的函数：more_stuff.pop() <=> pop(more_stuff)
#3.more_stuff.pop()：在more_stuff上调用pop函数；pop(more_stuff): 用more_stuff作为参数调用pop函数
#4. stuff[3:5] <=> range(3,5) : 切片：索引为3的元素取值，直到索引为4的元素

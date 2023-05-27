#字典：
#1. 改变list中的element
things = ['a', 'b', 'c', 'd']
print(things[1])
things[1] = 'z'
print(things[1])
print(things)

#b
#z
#['a', 'z', 'c', 'd']

#访问：字典可以通过任何东西（不只是数值）找到元素
stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
print(stuff['name']) #Zed

print(stuff['age']) #39

print(stuff['height']) #74

#通过数值，用字符串来从字典中获取stuff, 还可以用字符串往字典中添加因素
stuff['city'] = "SF"
print(stuff['city']) #SF

#增加/修改
stuff[1] = 'Wow'
stuff[2] = "Neato"
stuff['name'] = "Yuchen"
print(stuff[1]) #Wow
print(stuff[2]) #Neato
print(stuff)   # {'name': 'Yuchen', 'age': 39, 'height': 74, 'city': 'SF', 1: 'Wow', 2: 'Neato'}

#删除
del stuff['city']
del stuff[1]
del stuff[2]
print(stuff) #{'name': 'Yuchen', 'age': 39, 'height': 74}

#创建州字典
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
print(states) #{'Oregon': 'OR', 'Florida': 'FL', 'California': 'CA', 'New York': 'NY', 'Michigan': 'MI'}

#创建城市字典
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
print(cities) #{'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

#增加城市
cities['NY'] = 'New York'
cities['OR'] = 'Porland'
print(cities) #{'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville', 'NY': 'New York', 'OR': 'Porland'}

#打印一些城市 ※只能通过key找value，不能反向
print('-' * 10)                      #----------
print("NY State has:", cities['NY']) #NY State has: New York
print("OR State has:", cities['OR']) #OR State has: Porland

#打印一些州
print('-' * 10)
print("Michigan's abbreviation is:", states['Michigan']) #Michigan's abbreviation is: MI
print("Floria's abbreviation is:", states['Florida']) #Floria's abbreviation is: FL

#州->城市字典
print('-' * 10)
print("Michigan has:", cities[states['Michigan']]) #Michigan has: Detroit
print("Florida has:", cities[states['Florida']]) #Florida has: Jacksonville

#打印每州简称 for a,b in list(dictionary.item())
print('-' * 10)
print(states) #states = {'Oregon': 'OR', 'Florida': 'FL', 'California': 'CA', 'New York': 'NY', 'Michigan': 'MI'}
print(states.items()) #dict_items([('Oregon', 'OR'), ('Florida', 'FL'), ('California', 'CA'), ('New York', 'NY'), ('Michigan', 'MI')])
print(list(states.items()))#!!![('Oregon', 'OR'), ('Florida', 'FL'), ('California', 'CA'), ('New York', 'NY'), ('Michigan', 'MI')]
print(states.values()) #dict_values(['OR', 'FL', 'CA', 'NY', 'MI'])
for state, abbrev in list(states.items()):
    print(f" {state} is abbreviated {abbrev}")
# ----------
 # Florida is abbreviated FL
 # California is abbreviated CA
 # New York is abbreviated NY
 # Michigan is abbreviated MI

#打印每个州的城市
print('-' * 10)
print(list(cities.items())) #[('CA', 'San Francisco'), ('MI', 'Detroit'), ('FL', 'Jacksonville'), ('NY', 'New York'), ('OR', 'Porland')]
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
# ----------
# CA has the city San Francisco
# MI has the city Detroit
# FL has the city Jacksonville
# NY has the city New York
# OR has the city Porland

#同时做两种
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} sate is abbreviated {abbrev}")
    print(f"and has ciy {cities[abbrev]}")

#----------
# Oregon sate is abbreviated OR
# and has ciy Porland
# Florida sate is abbreviated FL
# and has ciy Jacksonville
# California sate is abbreviated CA
# and has ciy San Francisco
# New York sate is abbreviated NY
# and has ciy New York
# Michigan sate is abbreviated MI
# and has ciy Detroit

#.使用get；if not指令：【？】
print('-' * 10)
state = states.get('Texas')  #.get来获取不存在的键的值

if not state:
    print("Sorry, no Texas.")
# ----------
# Sorry, no Texas.

# get a city with a default value【？】
city = cities.get('TX', 'Does Not Exist') #.get来获取不存在的键的值并指定默认值
print(f"The city for the state 'TX' is: {city}") #The city for the state 'TX' is: Does Not Exist


#1.字典是一种，将一些项/键对应到另一些项(值)，映射或者关联起来数据结构。
#2.列表是一些项的有序排列。
#3.列表是专供需要有序排列的数据使用。只要知道索引就能查到对应的值了。







###################################################
# # 创建一个字典
# my_dict = {"apple": 3, "banana": 2, "orange": 1}
#
# # 访问字典中的值
# print(my_dict["apple"])    # 输出 3
#
# # 修改字典中的值
# my_dict["banana"] = 5
# print(my_dict["banana"])   # 输出 5
#
# # 添加新的键值对
# my_dict["grape"] = 4
# print(my_dict["grape"])    # 输出 4
#
# # 删除键值对
# del my_dict["orange"]
# print(my_dict)             # 输出 {"apple": 3, "banana": 5, "grape": 4}
###################################################
#.get的用法：
# 创建一个字典
# my_dict = {"apple": 3, "banana": 2, "orange": 1}
#
# # 获取存在的键的值
# print(my_dict.get("apple"))   # 输出 3
#
# # 获取不存在的键的值
# print(my_dict.get("grape"))   # 输出 None
#
# # 获取不存在的键的值并指定默认值
# print(my_dict.get("grape", 0))  # 输出 0

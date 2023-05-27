#函数和变量

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#P1:直接给函数传递数字
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

#P2:给它变量
print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#P3:给数据表达式
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#P4:数学表达式和变量组合
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# PS C:\Users\miran\lpthw> python ex19.py
# We can just give the function numbers directly:
# You have 20 cheese!
# You have 30 boxes of crackers!
# Man that's enough for a party!
# Get a blanket.
#
# Or, we can use variables from our script:
# You have 10 cheese!
# You have 50 boxes of crackers!
# Man that's enough for a party!
# Get a blanket.
#
# We can even do math inside too:
# You have 30 cheese!
# You have 11 boxes of crackers!
# Man that's enough for a party!
# Get a blanket.
#
# And we can combine the two, variables and math:
# You have 110 cheese!
# You have 1050 boxes of crackers!
# Man that's enough for a party!
# Get a blanket.

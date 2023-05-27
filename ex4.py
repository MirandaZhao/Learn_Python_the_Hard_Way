# ex4
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers  # 未使用车 = 车 - 司机
cars_driven = drivers  # 驾驶车数 = 司机数
carpool_capacity = cars_driven * space_in_a_car  # carpool储量 = 驾驶车数 * 每辆车座位数
average_passengers_per_car = passengers / cars_driven  # 平均每辆车乘客数 = 乘客数 / 驾驶车数

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#1.remove s from "average_passengers_per_car" to "average_passenger_per_car" returns error:
# Traceback (most recent call last):
#   File "C:\Users\miran\lpthw\ex4.py", line 16, in <module>
#     print("We need to put about", average_passengers_per_car, "in each car.")
#                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^
# NameError: name 'average_passengers_per_car' is not defined. Did you mean: 'average_passenger_per_car'?

#2.if I add random / in the line, return error:
#   File "C:\Users\miran\lpthw\ex4.py", line 24
#     \
# SyntaxError: unexpected EOF while parsing

#3.Using Atom ctrl+T returns all files

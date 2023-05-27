class Animal(object):
    pass

class Dog(Animal):

    def __init__(self, name):
        self.name = name

class Cat(Animal):

    def __init__(self, name):
        self.name = name

class Person(object):

    def __init__(self,name):
        self.name = name
        self.pet = None

class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()

# 这段代码是一个简单的 Python 类继承示例，它定义了多个类。
# 其中 Animal、Dog、Cat、Person、Employee、Fish、Salmon 和 Halibut 都是类名。
#   其中，Animal、Dog、Cat 是动物类，Person、Employee 是人类，Fish、Salmon 和 Halibut 是鱼类。
#
# 在这些类中，Dog 和 Cat 继承自 Animal 类，即狗和猫都是动物的一种。Person 和 Employee 继承自 Person 类，即员工和普通人都是人类的一种。
#   Fish、Salmon 和 Halibut 之间是继承关系，即鲑鱼和比目鱼都是鱼类的一种。
#
# 代码还定义了多个实例，如 rover 是一个名为 Rover 的狗，satan 是一个名为 Satan 的猫，mary 是一个名为 Mary 的人，并拥有一个宠物，这个宠物是 Satan。
#   frank 是一个名为 Frank 的员工，其薪水为 120000 美元，并拥有一个宠物，这个宠物是 Rover。
#   还有 flipper、crouse 和 harry 分别是 Fish、Salmon 和 Halibut 的实例，但没有任何属性或方法。

# 这个示例主要展示了类和继承的基本概念，以及如何创建和使用实例。



# super() 是一个内置函数，用于调用父类的方法。在 Python 3 中，可以使用 super() 函数来访问父类的属性和方法。
# 它的常用用法是在子类的方法中调用父类的方法，可以在子类中对父类的方法进行扩展或者重写。
#
# super() 函数需要两个参数，第一个参数是子类对象，第二个参数是子类对象所在的类。
# 例如，在下面的代码中，MySubclass 是 MyParentClass 的子类，my_object 是 MySubclass 的实例，

# 我们可以使用 super() 函数在子类的 my_method() 方法中调用父类的 my_method() 方法：
# 可以看到，MySubclass 的 my_method() 方法在调用父类的 my_method() 方法后，添加了自己的逻辑。
# 这样可以在不影响父类行为的情况下扩展子类的功能。

# class MyParentClass:
#     def my_method(self):
#         print('This is a parent method')
#
# class MySubclass(MyParentClass):
#     def my_method(self):
#         super().my_method()  # 调用父类的方法
#         print('This is a subclass method')
#
# my_object = MySubclass()
# my_object.my_method()
#
# This is a parent method
# This is a subclass method

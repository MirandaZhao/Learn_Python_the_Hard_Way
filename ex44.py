#隐式继承：
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# PARENT implicit()
# PARENT implicit()

#显示覆盖：
class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

        def override(self):
            print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()

# PARENT override()
# CHILD override()

#在运行前或运行后替换
class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("Child, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("Child, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()

# PARENT altered()
# Child, BEFORE PARENT altered()
# PARENT altered()
# Child, AFTER PARENT altered()

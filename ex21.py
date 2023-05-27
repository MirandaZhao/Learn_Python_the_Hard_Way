def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
print(">>> age", age)
height = subtract(78, 4)
print(">>> height=", height)
weight = multiply(90, 2)
print(">>> weight=", weight)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#iq = 100/2 = 50
print("That becomes: ", what, "Can you do it by hand?")

# PS C:\Users\miran\lpthw> python ex21.py
# Let's do some math with just functions!
# ADDING 30 + 5
# SUBSTRACTING 78 - 4
# MULTIPLYING 90 * 2
# DIVIDING 100 / 2
# Age: 35, Height: 74, Weight: 180, IQ: 50.0
# Here is puzzle.
# DIVIDING 50.0 / 2
# MULTIPLYING 180 * 25.0
# SUBSTRACTING 74 - 4500.0
# ADDING 35 + -4426.0
# That becomes:  -4391.0 Can you do it by hand?

#Puzzle:
# >>> iq = 50
# >>> weight = 180
# >>> height = 74
# >>> age = 35
# >>> iq / 2
# 25.0
# >>> weight * 25
# 4500
# >>> height - 4500
# -4426
# >>> age + -4426
# -4391
#>>> quit()




#input()
#int(input())
#float(input())

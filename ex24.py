print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------------")
print(poem)
print("--------------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(standard):
    jelly_beans = standard * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)                                #jelly_beans变成beans，因为函数内部的变量都是临时的。
                                                                                 #当函数返回之后，返回值可以被附与一个变量。这里穿件了一个beans
                                                                                 #的新变量，用来存放函数的返回值。

print("With a starting point of:{}".format(start_point))

print(f"We'd have {beans} beans, {jars} jars, an {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)

print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

# PS C:\Users\miran\lpthw>  python ex24.py
# Let's practice everything.
# You'd need to know 'bout escapes with \ that do:
#
#  newlines and    tabs.
# --------------------
#
#         The lovely world
# with logic so firmly planted
# cannot discern
#  the needs of love
# nor comprehend passion from intuition
# and requires an explanation
#
#                 where there is none.
#
# --------------------
# This should be five: 5
# With a starting point of:10000
# We'd have 5000000 beans, 5000.0 jars, an 50.0 crates.
# We can also do that this way:
# We'd have 500000.0 beans, 500.0 jars, and 5.0 crates.

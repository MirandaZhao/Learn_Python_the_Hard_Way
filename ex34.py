#访问列表中的元素
animals = ['bear', 'cat', 'peacock', 'kangaroo', 'whale', 'platypus']

i = int(input(">"))
select_animal = animals[i]
print(f"The {i+1} animal is at the position {i}, which is a", select_animal)
print(f"The {i+1} animal is at the position {i}, which is a {select_animal}." )
print(select_animal)

#PS C:\Users\miran\lpthw> python
# >>> bugs = ["ant", "firefly", "beetle"]
# >>> bugs[0]
# 'ant'
# >>> bugs[0]
# 'ant'
# >>> # OFF BY ONE
# >>> for bug in bugs:
# ...     print(bug)
# ...
# ant
# firefly
# beetle
# >>> bug[1]
# 'e'
# >>> bugs[1]
# 'firefly'
# >>> bugs[1:]
# ['firefly', 'beetle']
# >>> bugs[0:2]
# ['ant', 'firefly']
# >>> bugs[:2]
# ['ant', 'firefly']
# >>> bugs[:]
# ['ant', 'firefly', 'beetle']
# >>> bugs[-1]
# 'beetle'
# >>> bugs[0]
# 'ant'
# >>> bugs[-1]
# 'beetle'
# >>> bugs[-2]
# 'firefly'
# >>> bugs[-3]
# 'ant'
# >>> bugs[::-3]
# ['beetle']
# >>> bugs[::-1]
# ['beetle', 'firefly', 'ant']
# >>> bugs[::-2]
# ['beetle', 'ant']
# >>> bugs[-0::-2]
# ['ant']
# >>> bugs[-0:-3:-2]
# []
# >>> hello = "Hello World How Are You Today"
# >>> hello.split(' ')
# ['Hello', 'World', 'How', 'Are', 'You', 'Today']
# >>> hello.split(' ')[1]
# 'World'
# >>> #most common way to access
# >>> bugs[1:3]
# ['firefly', 'beetle']
# >>> bugs[0]
# 'ant'
# >>>

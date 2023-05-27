# ex6

# assgin 10 to types_of_people
types_of_people = 10
#assign the f-string to x (insert types_of_people in the string)
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
#print(">>> after assign y",y)

print(x)
#print(">>> before printing y",y)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'.")

hilarious = False
joke_evaluation = "Isn't that joke so funny? {}!"
print(joke_evaluation.format(hilarious))  # Isn't that joke so funny? False!
# A = a  B="b{}"  print(B.format(A)) --> b a

w = "This is the left side of..."
e = "a string with a right side"
print(w + e)  # 两个string可以相加相连

hilarious = True
joke_evaluation = "Isnt that joke so funny? {}!"
print(joke_evaluation.format(hilarious))

#1. line 10 remove f returns:
#I also said: 'Those who know {binary} and those who {do_not}.'.

#2. after remove f, I add debug printing:
# in line 11:print(">>> after assign y",y)
# and in line 14: print(">>> before printing y",y)
# returns >>> after assign y Those who know {binary} and those who {do_not}.
# and >>> before printing y Those who know {binary} and those who {do_not}.

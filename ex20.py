#Function and Files
#为什么output是乱码呢？
from sys import argv

script, input_file = argv

def print_all(f):
    print(">>> print_all: f=", f)
    print(f.read())
    print("<<< print_all: f", f)

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# PS C:\Users\miran\lpthw> python ex20.py test.txt
# First let's print the whole file:

# ÿþ
# Now let's rewind, kind of like a tape.
# Let's print three lines:
# 1 ÿþ
# 2
# 3
# PS C:\Users\miran\lpthw>

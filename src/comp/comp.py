# The following list comprehension exercises will make use of the
# defined Human class.
import math
import re


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"


humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]
print(humans)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
for human in humans:
    if(human.name[0:1] == 'D'):
        a.append(human.name)
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
for human in humans:
    nLength = len(human.name)
    if(human.name[nLength - 1:nLength] == 'e'):
        b.append(human.name)
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []
chars = ['C', 'D', 'E', 'F', 'G']
# humans[2].name[0:1] == chars[0]) == true
print(chars[0])
print(humans[2].name[0:1])
for human in humans:
    if(human.name[0:1] in chars):
        c.append(human.name)

print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [
]
for human in humans:
    if(human.age > 10):
        d.append(human.age)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
for human in humans:
    e.append(f'{human.name} - {human.age}')
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
for human in humans:
    if(human.age > 27 and human.age < 32):
        tup = (human.name, human.age)
        f.append(tup)
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []
for human in humans:
    newHuman = Human(human.name.upper(), (human.age + 5))
    g.append(newHuman)
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
h = []
for human in humans:
    h.append(math.sqrt(human.age))
print(h)

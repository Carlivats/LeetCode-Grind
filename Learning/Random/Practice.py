# This is my first time coding from scratch on python!

x = 10.2
y = "Coding"
print(y)

# Casting
y = str(10)

# Strings work with both ' and ""

# Case Sentitive - Capital letters matter
A = "Python"
a = "Variables"

print(A)
print(a)

# Data types are built-in
print(type(a))
print(type(x))

# Multi-line Strings
A = """ something something somerthing
More something silly me"""

# No Characters on py
a = "Hello World"
print(a[0])
print(len(a))

# Booleans
print(10 < 9)

if a == 100:
    print(True)

print(bool(""))

# Operators

a = ["Apple"]
b = ["Banana"]

print(a+b)

# assigment operators

x += 1
x += 1

# Lists
list = ["apple","Banana","Microsoft"]

print(list)
print(len(list))
print(list[0])

# Tuples: Multiple items on one variable

tuple_example = ('Noelia',)
print(tuple_example)

print(len(tuple_example))
print(type(tuple_example))

# Sets: collections of data unordered, unindex

set = {'otra','noche','en','miami','en'}

print(set)
print(len(set))

# Dictionaries: 3.7 later. 
dictionary = {
    "brand" : "Chevrolet",
    "model" :"Aveo",
    "year": 2007
}

print(dictionary)
print(dictionary["model"])

a = 100
b = 200

if b > a:
    print ("Ahhhh")
elif a < b:
    print("Hooo")
else:
    print()

# loops
i = 0
while i <= 100:
    print(i)
    i+=1
    if i == 2:
        break
i = 0
for x in list:
    print(x)

for x in "banana":
    print(x)

# Functions

def function(name):
    print(name)

function("Noelia")

class MyClass():
    x = 5

new = MyClass()

print(new.x)

def functio2n(u, z=0):
    x = 30 + u
    y = x * 3 + z
    return x , y

var1, var2 = functio2n(6,1)

print(var1, var2)

# Unpack operator

def func(x, y):
    print(x,y)

x = [1,2,3,4,5]
print(x,*x)

pair = [(1,2),(3,4)]

x = "tim"

try:
    x = 7 / 0
except Exception as e:
    print(e)

# fstrings

x = f"Noelia is {x}"
print(x)
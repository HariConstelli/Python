'''
Python Dictionary is a data structure that stores the value in key:value pairs. Values in a dictionary can be of
Any datatype and can be duplicated. Whereas Keys can't be repeated and must be immutable.


a = {1:'Hari', 2:'Krishna', 3:1234567}
print(a)

d2 = dict(a = 'Hari', b = 'for', c = 'Krishna')
print(d2)

d = { "name": "Prajjwal", 1: "Python", (1, 2): [1,2,4] }
print(d[1])

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"

print(d)

#Set is an unordered collection of multiple items having different datatypes. In Python, sets are mutable and unindexed
and do not contain duplicates. The order of elements in a set is not preserved and can change

set1 = {1,2,3,4}
print(set1)

set1 = set()
print(set1)

set1 = set("Geeksfor Hyderabad")
print(set1)

tup = ("Geeks", "For", "Hyderabad")
print(set(tup))

set1 = set(['Geeks', 'for', 'Hyderabad'])
print(set1)

d = {'Geeks':1, 'For':2, 'Hyderabad':3}
print(set(d))

set1 = {1,2,3}
set1.add(4)
set1.update([5,6])

print(set1)

#Accessing set in Python

set1 = set(["Geeks", 'For', "Geeks."])

for i in set1:
    print(i, end=" ")

print('Geeks' in set1)

#Removing elements from the set in PYthon'''

set1 = {1,2,3,4,5}
set1.remove(3)
print(set1)

try:
    set1.remove(10)
except KeyError as e:
    print('Error', e)

set1.discard(4)
print(set1)

set1.discard(10)
print(set1)

#Pop() method

set1 = {1,2,3,4,5}
val = set1.pop()
print(val)
print(set1)

set1.clear()
try:
    set1.pop()
except KeyError as e:
    print("Error", e)

set1 = {1,2,3,4,5}
set1.clear()
print(set1)

#Typecasting Objects into Sets

li = [1,2,3,3,5,6,6,8,9]
set1 = set(li)
print(set1)

s = "GeeksforGeeks"
set1 = set(s)
print(set1)

d = {1:'One', 2:'Two', 3:'Three'}
set1 = set(d)
print(set1)

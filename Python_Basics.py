#Python is a High level programming language invented by Guido Van Rossum in 1991

#First Program In Python
'''
name = input('Enter your name:')
print("Hi", name, 'Welcome to Python')

#Variable : Variables acts a Placeholders for data

age = 30
'age is a variable which is assigned to that value 30'

#Python Datatypes

Numeric Datatypes: int(), float(), complex()

a = 10
print(int(a))
print(float(a))
print(complex(a))

output 
10
10.0
(10+0j)

Sequence Type:  String, List, tuple

String = 'String is a Sequence Data Type'

List = [1,2,'1','b',30.1, 10+0j]

tuple = (1,2,'a','b', 30)

Mapping Datatype = dict()

Dict is key, value pair = {1:10, 2:20, 3:'abc'}

Boolean Datatype = bool

#True or False

#Set datatype

set = {1,2,3,'a','b'}


Type Converstion: Conversion of one datatype into another datatype

a = '10'
b = int(a)
print(type(b))

x = 10.20
y = int(x)
print(type(y))

output:
<class 'int'>
<class 'int'>

a = 10
b = 10.25
x = str(a)
y = str(b)
print(type(x))
print(type(y))

output:
<class 'str'>
<class 'str'>


#String: A String is a sequence of characters enclosed in quotes.
s1 = 'Hari'
s2 = 'Krishna'

print(s1)
print(s2)

#Accessing Characters in String

print(s1[0])
print(s2[2])

#Negetive Indexing

print(s1[-1])
print(s2[-2])

#String Slicing
print(s1[1:4])
print(s2[-1:-3])

#Reverse a String
print(s1[::-1])
print(s2[::-1])

#Conditional Statements in Python
#Conditional Statements are used to execute certain blocks of code based on specific conditions

#If conditions
age = 20
if age >= 18:
    print("Eligible to Vote")

#If else allows us to specilfy a block of code that will execute if the conditions associated with if and elif statements evaluates to False

age = 10
if age <= 12:
    print('Travel for free')
else:
    print('Pay for ticket')

#elif statement
#Elif statement in Python Stands for 'else if'. It allows us to check multiple conditions, providing a way to execute different blocks of code based on which condition is true.

age = 25
if age <= 12:
    print('Child')
elif age <= 19:
    print('Teenager')
elif age <= 35:
    print('Young Adult')
else:
    print('Adult')

#Operators in Python
#Arithematic Operators
a = 15
b = 4
print('Addition:', a+b)
print('Substraction:', a-b)
print('Multiply:', a*b)
print('Division:', a/b)
print('Floor division:', a//b)
print('Modulos:', a%b)
print('Exponentiation:', a**b)

#Comparison Operators
a = 13
b = 33
print(a >b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

#Logical Operators 'and' 'or' 'not'

a = True
b = False
print(a and b)
print(a or b)
print(not a)
'''
#Python Bitwise Operators
a = 10
b = 2
print('Bitwise AND', a & b)
print('Bitwise OR', a | b)
print('Bitwise Not', ~a)
print('Bitwise XOR', a ^ b)
print('Bitwise right shift', a>>b)
print('Bitwise left shift', a << b)
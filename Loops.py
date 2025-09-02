'''
Loops in Python are used to repeat actions efficiently. The Main types are For Loops and While Loops

For Loop:
For loops is used to iterate over a sequence such as a list, tuple, string or range. It allows to
execute a block of code repeatedly, once for each item in the sequence.

for i in range(4):
    print(i)

li = ['constelli', 'madhapur', 'hyd']
for i in li:
    print(i)

li = ('constelli', 'madhapur', 'Hyd')
for i in li:
    print(i)

s = 'Constelli'
for i in s:
    print(i)

d = dict({'x':123, 'y':354})
for i in d:
    print("%s %d"%(i, d[i]))

set1 = {1,2,3,4,5,6}
for i in set1:
    print(i)


#While Loop: A While loop is used to execute the block of statements repeatedly until a given condition is satisfied.

#Example
cnt = 0
while cnt < 3:
    cnt = cnt + 1
    print('Hello Constelli')

#Using else statement with while loop
cnt = 0
while (cnt < 3):
    cnt = cnt+1
    print('Hello Constelli')
else:
    print('In Else block')

#Nested Loops: Python Allows to use one loop inside another loop which i called nested loop

for i in range(5):
    for j in range(i):
        print(i, end=" ")
    print()

#Loop Control Statements

#The Continue Statement in Python returns the control to the beginning of the loop

for letter in 'constelli signals private limited':
    if letter == 'e' or letter == 'p':
        continue
    print('Current letter:', letter)

#The Break Statement in Python brings control out of the loop

for letter in 'constelli':
    if letter == 's' or letter == 'o':
        break
print('Current Letter:', letter)

#Pass Statement: We use Pass statement in Python to write empty loops. Pass is also used for empty control statements, functions and classes.

for letter in 'geeksforgeeks':
    pass
print('Last letter:', letter)'''

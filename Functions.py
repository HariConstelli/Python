'''Python Functions is a block of statements that does a specific task.
Types of functions:
Built in library function: These are Standard functions in python that are available to use.
User-defined funcations: We can create our own functions based on our requirements


def even_odd(x : int) ->str:
    if (x%2 == 0):
        return 'Even'
    else:
        return 'Odd'
    
print(even_odd(16))
print(even_odd(9))

There 4 types of arguments
1.default arguments
2.Keyword arguments
3.Positional Arguments
4.Arbitary Keyword arguments *args and **kwargs

#Recursive Functions


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

Python Lambda Functions

Lambda functions are anonymus functions means that means the function without a name.



s1 = 'constelli'
s2 = lambda x: x.upper()
print(s2(s1))

li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())

calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)

n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))

a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))

The map() function takes a function and list as an argument

Reduce:

the reduce function is python takes in a function and a list as an argument
'''
from functools import reduce
a = [1,2,3,4]
b = reduce(lambda x,y:  x*y, a)
print(b)
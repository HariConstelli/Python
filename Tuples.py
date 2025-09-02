'''A Tuple in Python is an Immutable ordered collection of elements
Tuples are  similar to lists, but unlike lists, they cannot be changed aftr their creation
Tuples can hold elements of different data types
The main characteristics of tuples are being ordered, heterogeneous and Immutable
tup = ()
print(type(tup))

tup = ("Geeks", 'For')
print(tup)

li = [1,2,3,4,5,6]
print(tuple(li))

tup = tuple('Geeks')
print(tup)

tup = (5,'Welcome', 7, 'Geeks')
print(tup)

tup1 = (0,1,2,3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)

tup1 = ('Hari',) * 3
print(tup1)

tup = ("Geeks")
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)

#Accessing Tuple with Indexing

tup = tuple('HariKrishna')
print(tup[:5])

#Concatination of Tuples
tup1 = (0,1,2,3)
tup2 = ('Geeks', 'For', 'Hari')

tup3 = tup1+tup2
print(tup3)

#Slicing a tuple means creating a new tuple from a subset of elements of the original tuple syntax tuple[start:stop:step]

tup = tuple('GeeksForHari')
print(tup[1:])
print(tup[::-1])
print(tup[4:7])'''


x,y,z = (1,2,3)
print(x)
print(y)
print(z)

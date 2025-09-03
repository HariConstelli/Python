'''#Class: A class is a collection of objects. Classes are blueprints for creating objects. 
A class defines a set of attributes and methods that the created objects can have.

class Dog:
    species = 'Canine'
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

#An Object is an Instance of a class. It represents a specific implementation of the class and holds its own data.
State: It is represented by the attributes and reflects the properties of an object.
Behavior : It is represented by the methods of an object and reflects the response of an object o other objects.
Identity: It gives a unique name to an object and enables one object to interact with other objects

class Dog:
    species = 'Canine'
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog('Buddy', 3)
print(dog1.name)
print(dog1.species)


Self parameter is a referance to the current instance of the class. It Allows us to access the
attributes and methods of the object


class Dog:
    species = 'Canine'
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog('Buddy', 3)
dog2 = Dog('Charlie', 5)

print(dog1.name, dog1.age, dog1.species)
print(dog2.name, dog2.age, dog2.species)
print(Dog.species)

Class Variables: These are the variables that are shared across all instances of a class.
It is defiend at class level, outside any methods.

Instance Variables: Variables that are unique to each instance of a class.



class Dog:
    species = 'Canine'
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1.species)
print(dog1.name)
print(dog1.age)

dog1.name = 'Maxx'
print(dog1.name)

Dog.species = 'Feline'
print(dog1.species)
print(dog2.species)


#Inheritance: Inheritance allows a class (child class) to acquire properties and methods of another class

class Dog:
    def __init__(self,name):
        self.name = name
    def display_name(self):
        print(f"Dogs Name: {self.name}")

class Labrador(Dog):
    def sound(self):
        print('Labrador Woofs')

class Guidedog(Labrador):
    def guide(self):
        print(f'{self.name} Guides the way!')

class Friendly:
    def greet(self):
        print('Friendly!')

class GoldenRetriver(Dog, Friendly):
    def sound(self):
        print('Golden Retriver Barks')

lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog  = Guidedog('Max')
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriver('Charlie')
retriever.display_name()
retriever.greet()
retriever.sound()


#Polymorphism allows methods to have the same name but behave differently based on the objects context.

Types of Polymorphism

Complie time polymorphism

Run time polymorphism

class Dog:
    def sound(self):
        print('dog sound')

class Labrador(Dog):
    def sound(self):
        print('Labrador')

class Beagle(Dog):
    def sound(self):
        print('Beagle Barks')

class Calculator:
    def add(self, a, b= 0, c=0):
        return a+b+c
    
dogs = [Dog(), Labrador(), Beagle()]
for dog in dogs:
    dog.sound()


ENCAPSULATION: Encapsulation is the bundling of data and methods within a class, restricting access to some components to control interactions.



class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self._breed = breed
        self.__age = age

    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age:{self.__age}"
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print('Invalid age!')

dog = Dog('Buddy', 'Labrador', 3)

print(dog.name)

print(dog._breed)

print(dog.get_age())

dog.set_age(5)
print(dog.get_info())

Data Abstraction:

Abstraction hides the Internal implementation and shows the necessary functionality. It helps focus on what to do rather than how to do it.

types"
Partial Abstraction: Abstract class contains both abstract and concrete methods.

Full Abstraction: Abstract class contains only abstract methods.

'''

from abc import ABC, abstractmethod

class Dog(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def sound(self):
        pass

    def display_name(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):
        def sound(self):
            print('Labrador Woof!')

class Beagle(Dog):
     def sound(self):
          print("Beagle Bark!")

dogs = [Labrador('Buddy'), Beagle('Charlie')]
for dog in dogs:
     dog.display_name()
     dog.sound()
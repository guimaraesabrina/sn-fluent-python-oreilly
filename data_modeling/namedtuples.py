"""
Namedtuples in Python are a way to create immutable classes with named fields.

They are a variation of common tuples, which are ordered, immutable collections of elements. 

The main difference is that, in a namedtuple, you can assign names to individual elements.
"""

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])

person1 = Person(name='Sabrina', age='21')
person2 = Person(name='Maria', age='90')

print(person1.name)
print(person2.age)

"""
One of the advantages of namedtuples is that they are immutable, that is, once you create an instance, you cannot change it. 
This can be useful to ensure that data is not inadvertently changed somewhere in the code.

"""

print(person1) #Person(name=Sabrina, age=21)

"""
The main difference between namedtuples and classes in Python is that namedtuples are immutable whereas classes are generally mutable.

Immutability means that objects cannot be changed once they are created. In the case of namedtuples, this means that their values cannot be modified directly, which ensures that instances always remain consistent and predictable.

On the other hand, Python classes often allow their attributes to be modified at runtime, which can make the code more flexible, but also more complex and difficult to maintain.

"""

# namedtuple and class (the diff)

# namedtuple 
NTPoint = namedtuple('NTPoint', ['x', 'y'])
point = NTPoint(1,2)
print(point.x, point.y)

#class 
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y 

point_cls = Point(1, 2)
print(point_cls.x, point_cls.y)

# we access classes and namedtuples in the same way

print(point.x, point.y)
print(point_cls.x, point_cls.y)

point.x = 3 # not allowed in namedtuple as they are immutable
point_cls.x = 3 # allowed in classes as they are mutable

# briefly: namedtuples cannot receive new methods or new values as they are 100% immutable
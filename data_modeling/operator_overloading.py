"""
Operator Overloading in Python

With operator overloading, you can allow two objects of a custom class to be added using the + operator.

This allows objects created from these classes to behave like built-in data types (such as numbers, strings, and lists) with respect to common operators.

"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # now v3 is a Vector object with the values (4, 6)

"""
In this case, I just summed two objects with operator overloading. 

https://www.programiz.com/python-programming/operator-overloading

"""
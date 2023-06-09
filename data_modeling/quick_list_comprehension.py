"""
List comprehension

List comprehension is a concise way to create lists in Python using an expression enclosed in square brackets []. 
This expression usually includes a for loop and, optionally, an if condition.

When to use:

1. When you want to create a new list based on another collection, such as a list, tuple, or dictionary, and the transform or filter expression is simple and easy to understand.

2. When you want to apply a function to all elements of a collection and create a new list with the results.

3. When you want to filter elements from a collection based on a simple condition, and the condition is clear and concise.

When not to use:

1. When the transform or filter expression is complex, with multiple nested conditions or operations. In these cases, a traditional for loop can make the code more readable.

2. When you want to modify an existing list instead of creating a new one. List comprehensions are designed for creating new lists, not for modifying existing lists. In these cases, a for loop or other list operations may be more appropriate.

3. When you want to create a list based on multiple collections of data. While it is possible to use nested list comprehensions, this can make the code difficult to read and understand.

And more... 

"""

"""
Exact Structure:

1. The exact structure of a list comprehension in Python consists of three main parts, enclosed in square brackets [].

2. output expression: The expression that defines the value of each element in the resulting list. This expression can be a function, a mathematical operation, or any other expression that returns a value.

3. for loop: A for loop that iterates over a sequence, such as a list, tuple, or range object. The iteration variable is used in the output expression to calculate the value of each element in the resulting list.

4. if condition (optional): An optional condition that can be used to filter elements from the input sequence. If the condition is true, the output expression is applied to the sequence element and added to the resulting list. If the condition is false, the element is ignored.

Best example:
[output_expression for iteration_variable in sequence if condition]

"""
# Example:

ranks = [str(n) for n in list(range(2, 11)) + list('JQKA')] 

"""
This line of code creates a ranking list of playing cards, which consists of numbers from 2 to 10, and letters 'J', 'Q', 'K' and 'A'.

Here, the range(2, 11) function generates numbers from 2 to 10.

We then convert the range object to a list and concatenate it with the list ['J', 'Q', 'K', 'A'].

The result:

"""

['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# More examples: 

[x ** 2 for x in range(10)] 
"""
Squares of numbers from 0 to 9
Raises each number in the sequence of numbers created in range(10) by 2

"""

[x for x in range(1, 21) if x % 2 == 0]
"""
'x' = This is the output expression of the list comprehension, which in this case is simply the iteration variable x

'for x in range(1, 21)' = This is the for loop that iterates over the sequence of numbers generated by the range(1, 21) object. The sequence starts at 1 and goes up to 20 (not including 21). The iteration variable x takes on the value of each element in the sequence during the iteration.

'if x % 2 == 0:' This is the optional if condition that filters elements from the input sequence. In this case, the condition is true only for even numbers, that is, when the remainder of dividing x by 2 is equal to 0.

The result: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

"""





"""
The collections module is a standard Python library that provides alternative and specialized data structures beyond the basic structures available in Python, such as lists, dictionaries, and tuples. 

Some of the most common data structures in the collections module are:

"namedpuble" = It is a subclass of a tuple, which allows you to access elements by name using dot notation (for example, object.field). Namedtuples are immutable and more memory efficient than regular dictionaries, making them ideal for storing simple records with named fields.

"deque" = A doubly-ended queue (also known as a deque, short for "double-ended-queue") is a data structure that allows you to insert and remove elements from both sides (front and end) efficiently. A deque is a generalization of a stack and a queue.

"Couter" = It is a specialized dictionary for counting the frequency of elements in a collection. It can be useful for counting the number of occurrences of each item in a list, for example.

"OrderedDict" = It is a dictionary that maintains the order of insertion of items. As of Python 3.7, the insertion order of items is preserved by default in common dictionaries, but OrderedDict can still be useful in earlier versions of Python or when you need to emphasize insertion order in your code.

"defaultdict" = It's a dictionary that provides a default value for keys that don't already exist in the dictionary. It's useful when you want to avoid missing key errors and simplify your code.

"ChainMap" = It is a class that encapsulates multiple dictionaries in a single mapping object. It's useful when you want to combine multiple mappings while keeping your original structure separate.

"""

import collections

col = collections

col.ChainMap
col.Counter
col.defaultdict
col.deque
col.UserString # and more...

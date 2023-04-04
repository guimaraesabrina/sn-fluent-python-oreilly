"""
Part of Python collections.

A doubly-linked queue (deque) is useful in many situations where you need fast and efficient insertions and removals at both ends of the data structure. Some common applications include:

     Work Queues: When you have a queue of jobs to be processed and the order of processing can be from either the front or the back of the queue, a deque is an appropriate choice.

     Sliding windows: In algorithms that process data sequences with a window of fixed size that slides along the sequence, a deque can be used to store the window elements, adding new elements on one side and removing old elements on the other.

     Undo/redo: In applications like text editors, where you want to keep a history of actions to allow undo/redo operations, a deque can be used to store the actions and access them in reverse order.

     Palindromes: When checking whether a string is a palindrome, you can use a deque to compare characters from the ends of the string to the middle.

     Capacity Constraints: A deque can be used with a maximum size to hold a limited number of elements, automatically removing the oldest element when adding a new element when the maximum capacity is reached. This can be useful for keeping a fixed-length history or caching information.

     Implementing stacks and queues: The deque can be used to easily implement stacks and queues, restricting operations to just one side. For a stack, you can append and pop on the same side, while for a queue, you can append on one side and popleft on the other.
"""

from collections import deque

# Create an empty deck
d = deque()

# Add elements to the beginning of the deque
d.appendleft(1)
d.appendleft(2)

# Add elements to the end of the deque
d.append(3)
d.append(4)

# Remove elements from the beginning of the deque
frst_element = d.popleft()

# Remove elements from the end of the deque
last_element = d.pop()

# Print current deck
print(d)  # deque([2, 1, 3])

"""
Briefly: When I want to extremely quickly access and manipulate the ends of my list, I use deque.
"""
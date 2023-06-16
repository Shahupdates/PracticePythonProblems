"""
Implement a Stack using Queues

Implement a stack data structure using queues. The stack should support the following operations: `push`, `pop`, `top`, and `empty`.
"""

from collections import deque

class Stack:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    def top(self):
        return self.queue[-1]

    def empty(self):
        return len(self.queue) == 0

# Create a stack object
stack = Stack()

# Perform stack operations
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.top())    # Output: 3
print(stack.pop())    # Output: 3
print(stack.empty())  # Output: False

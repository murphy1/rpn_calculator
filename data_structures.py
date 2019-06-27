# This file will contain the Stack data structure needed for our project


class Stack:
    """Basic stack class"""

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) is 0:
            return "The stack is empty"
        else:
            return self.stack.pop()

    def is_empty(self):
        if len(self.stack) is 0:
            return True
        else:
            return False


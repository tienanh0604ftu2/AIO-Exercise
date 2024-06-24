class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self._stack = []

    def is_empty(self):
        return len(self._stack) == 0

    def is_full(self):
        return len(self._stack) == self.capacity

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._stack.pop()

    def push(self, value):
        if self.is_full():
            raise OverflowError("push to full stack")
        self._stack.append(value)

    def top(self):
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self._stack[-1]


# Testing
stack1 = Stack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())

print(stack1.top())
print(stack1.pop())

print(stack1.top())
print(stack1.pop())

print(stack1.is_empty())
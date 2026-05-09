"""
Stack - LIFO (Last In, First Out) val structure.
Backed by a singly linked list; all operations act on the top (head) pointer.

| Operation | Time Complexity |
|-----------|----------------|
| push      | O(1)           |
| pop       | O(1)           |
| peek      | O(1)           |
| size      | O(1)           |
"""


class StackImpl:

    class Node:
        def __init__(self, val=None):
            self.val = val
            self.next = None

    def __init__(self):
        self.top = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0
        
    def push(self, val):
        newNode = self.Node(val)

        newNode.next = self.top
        self.top = newNode
        self._size += 1

    def pop(self):
        if self.isEmpty():
            return None
        toRemove = self.top
        self.top = self.top.next
        self._size -= 1
        return toRemove.val
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.top.val
    
    def size(self):
        return self._size
    
    def __iter__(self):
        current = self.top
        while current:
            yield current.val
            current = current.next

    def __str__(self):
        if self.isEmpty():
            return "Stack: []"
        return "Stack: [" + ", ".join(str(val) for val in self) + "]"
    
myStack = StackImpl()

print("Pushing 1:", myStack.push(1))
print(myStack)
print("Pushing 2:", myStack.push(2))
print(myStack)
print("Pushing 3:", myStack.push(3))    
print(myStack)

print("Popping stack:", myStack.pop())
print(myStack)

print("Peeking top element:", myStack.peek())
print("iterating over the stack:")
for item in myStack:
    print(item)



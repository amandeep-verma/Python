"""
Queue - FIFO (First In, First Out) data structure.
Backed by a singly linked list with head (front) and tail (back) pointers.

| Operation | Time Complexity |
|-----------|----------------|
| enqueue   | O(1)           |
| dequeue   | O(1)           |
| peek      | O(1)           |
| size      | O(1)           |
"""


class QueueImpl:

    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def isEmpty(self):
        return self._size == 0

    def enqueue(self, data):
        newNode = self.Node(data)
        if self.isEmpty():
            self.head = newNode
        else:
            self.tail.next = newNode

        self.tail = newNode
        self._size  += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        toRemove = self.head
        self.head = self.head.next
        self._size  -= 1
        if self.isEmpty():
            self.tail = None
        return toRemove.data

    def size(self):
        return self._size
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.head.data
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        if self.isEmpty():
            return "Queue: []"
        # Since we have __iter__, we can just do this:
        return "Queue: [" + " -> ".join(map(str, self)) + "]"
    

myQueue = QueueImpl()
print("Add items to the queue: 1",myQueue.enqueue(1))
print(myQueue)
print("Add items to the queue: 2",myQueue.enqueue(2))
print(myQueue)
print("Add items to the queue: 3",myQueue.enqueue(3))
print(myQueue)

print("Dequeue:", myQueue.dequeue())
print(myQueue)

print("iterating over the queue:")
for item in myQueue:
    print(item)
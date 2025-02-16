class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("stack underflow")

        curr = self.head
        if self.head == self.tail:
            data = self.tail.data
            self.head = self.tail = None
            return data

        while curr.next != self.tail:
            curr = curr.next
        data = self.tail.data
        curr.next = None
        self.tail = curr
        return data

    def is_empty(self):
        return self.head is None

    def top(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.tail.data

# Example usage:
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
print(my_stack.top())        # Output: 4
print(my_stack.is_empty())   # Output: False
print(my_stack.pop())        # Output: 4
print(my_stack.pop())        # Output: 3
print(my_stack.pop())        # Output: 2
print(my_stack.pop())        # Output: 1
print(my_stack.is_empty())   # Output: True2
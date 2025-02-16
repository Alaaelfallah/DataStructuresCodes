from doublyLinkedList import doublyLinkedList
class Stack:
    def __init__(self):
        self.items=doublyLinkedList()
    def push(self,data):
        self.items.append(data)
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError("stack undrflow")
    def top(self):
        return self.items.tail.data
    def size(self):
        return len(self.items)
my_stack = Stack()
my_stack.push("alaa")
my_stack.push("is")
my_stack.push("a")
my_stack.push("Great")
my_stack.push("Engineer")
print(my_stack.size())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.size())
print(my_stack.pop())


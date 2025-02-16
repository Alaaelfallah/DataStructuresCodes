class stackArr:
    def __init__(self,size):
        self.items=[None for _ in range(size)]
        self.top=-1

    def push(self,data):
        if (self.top)+1 == len(self.items):
            print("stack overflow")
            x=[None for _ in range(len(self.items))]
            self.items+=x
        self.items.append(data)
        self.top+=1

    def pop(self):
        if self.top==-1:
            raise  IndexError("stack underflow")
        else:
            data=self.items[self.top]
            self.top-=1
            return data
    def __len__(self):
        return (self.top)+1
    def __str__(self):
        current=self.items
        st="{"
        for x in current:
            st+=str(x)
            st += ","
        st += "}"
        return st



my_stack=stackArr(3)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack)
my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack)

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class doublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.tail=self.head=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.size+=1
    def insert(self,data,index=0):
        new_node=Node(data)
        if index<0 or index>self.size:
            raise IndexError('invalid index')
        if index ==0:
            if not self.head:
               self.tail= self.head=new_node
            else:
                new_node.next = self.head.next
                self.head.prev=new_node
                new_node = self.head
        elif index==self.size:
            self.append(data)
        else: #inserting in the middle
            current_node=self.head
            for _ in range(index):
                current_node=current_node.next
            new_node.next=current_node
            new_node.prev = current_node.prev
            current_node.prev.next=new_node
            current_node.prev=new_node
        self.size+=1
    def __str__(self):
        result=""
        current_node=self.head
        while current_node:
            result=result+str(current_node.data)+"->"
            current_node=current_node.next
        return result
    def remove(self,index):
        current_node=self.head
        for _ in range(index):
            current_node=current_node.next
        if current_node.next and current_node.prev: #in the middle
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
        elif current_node.next:                    #in the beggining
            self.head=current_node.next
            self.head.prev=None
        else:                                  #at the end
            self.tail=current_node.prev
            self.tail.next=None
        self.size-=1
    def __len__(self):
        return self.size
    def pop(self):
        data=self.tail.data
        if not self.tail:
            raise IndexError("pop from empty lit")
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head=self.tail=None
        self.size-=1
        return data
    def search(self,data):
        current=self.head
        while current:
            if current.data==data:
                return True
            current=current.next
        return False

if __name__=="__main__":
    my_linkedList=doublyLinkedList()
    my_linkedList.append("hi")
    my_linkedList.append("I")
    my_linkedList.append("am")
    my_linkedList.append("Alaa")
    my_linkedList.insert("everyone",1)
    my_linkedList.insert("lol",2)
    print(my_linkedList)
    my_linkedList.remove(2)
    print(my_linkedList)
    print(len(my_linkedList))
    my_linkedList.pop()
    print(my_linkedList)
    print(len(my_linkedList))
    print(my_linkedList.search('am'))





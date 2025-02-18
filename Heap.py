class MaxHeap:
    def __init__(self,capacity):
        self.tree=[None]*capacity
        self.capacity=capacity
        self.last_ele=-1
    def insert(self,value):
        if self.last_ele+1==self.capacity:
            print("heap overflow")
            return
        self.last_ele+=1
        self.tree[self.last_ele]=value
        i=self.last_ele
        while i>0:
            if self.tree[i]>self.tree[(i-1)//2]:
                self.tree[i] ,self.tree[(i - 1) // 2]=self.tree[(i-1)//2],self.tree[i]
                i=(i-1)//2
            else:
                break
    def max(self):
        return self.tree[0]
    def delete(self):
        if self.last_ele==-1:
            print("empty heap")
        elif self.last_ele==0:
            item=self.tree[0]
            self.tree[0]=None
            self.last_ele=-1
            return item
        else:
            item =self.tree[0]
            self.tree[0]=self.tree[self.last_ele]
            self.last_ele-=1
            i=0
            while i<=self.last_ele:
                if  self.tree[i*2+2]:
                    if self.tree[i*2+1]>self.tree[i*2+2]:
                        if self.tree[i*2+1]>self.tree[i]:
                            self.tree[i * 2 + 1],self.tree[i]=self.tree[i],self.tree[i*2+1]
                            i=i * 2 + 1
                        else:
                            break
                    else:
                        if self.tree[i * 2 + 2] > self.tree[i]:
                            self.tree[i * 2 + 2], self.tree[i] = self.tree[i], self.tree[i * 2 + 2]
                            i=i * 2 + 2
                        else:
                            break
                elif self.tree[i*2+1]:
                    if self.tree[i * 2 + 1] > self.tree[i]:
                        self.tree[i * 2 + 1], self.tree[i] = self.tree[i], self.tree[i * 2 + 1]
                        i=i * 2 + 1
                    else:
                        break
                else:
                    break
                return item

    def __repr__(self):
        if not self.tree or self.tree[0] is None:  # Check for empty tree
            return '<empty tree>'
        return '\n'.join(self.build_tree(0, 0))

    def build_tree(self, index, depth):
        result = []
        if index < self.capacity and self.tree[index] is not None:  # Check if the node exists
            result.append(' ' * (depth * 4) + str(self.tree[index]))  # Indent based on depth
            result.extend(self.build_tree(2 * index + 1, depth + 1))
            result.extend(self.build_tree(2 * index + 2, depth + 1))
        return result
# Example usage
if __name__ == "__main__":
    my_heap = MaxHeap(7)  # Array-based BST with capacity for 15 nodes
    my_heap.insert(50)
    my_heap.insert(30)
    my_heap.insert(20)
    my_heap.insert(40)
    my_heap.insert(70)
    my_heap.insert(60)
    my_heap.insert(80)
    my_heap.insert(80)

    print("BST Representation:\n", my_heap)

    # Delete a key
    print(my_heap.delete())
    print(my_heap.delete())
    print(my_heap.delete())
    print(my_heap.delete())
    print(my_heap.delete())
    print(my_heap.delete())
    print(my_heap.delete())
    print(my_heap.delete())










class ArrayBST:
    def __init__(self,capacity):
        self.tree=[None]*capacity
        self.capacity=capacity
    def insert(self,key):
        if self.tree[0]==None:
            self.tree[0]=key
        else:
            self._insert(0,key)
    def _insert(self,index,key):
        if index>self.capacity:
            raise IndexError("tree capacity exceeded")
        elif self.tree[index] == None:
            self.tree[index]=key
        elif key < self.tree[index]:
            left_index=2*index+1
            self._insert(left_index,key)
        elif key > self.tree[index]:
            right_index = 2 * index + 2
            self._insert(right_index, key)
    def search(self,key):
        return self._search(0,key)
    def _search(self,index,key):
        if index>=self.capacity:
            raise IndexError("the tree capacity is exceeded")
        if key==self.tree[index]:
            return index
        elif key<self.tree[index]:
            return self._search(index*2+1,key)
        elif key>self.tree[index]:
            return self._search(index*2+2,key)
    def delete(self, key):
        index = self.search(key)
        if index is not None:
            self._delete(index)

    def _delete(self, index):
        if self.tree[index] is None:
            return

        if self.tree[2 * index + 1] is None and self.tree[2 * index + 2] is None:
            self.tree[index] = None
        elif self.tree[2 * index + 1] is None:
            self.tree[index] = self.tree[2 * index + 2]
            self._delete(2 * index + 2)
        elif self.tree[2 * index + 2] is None:
            self.tree[index] = self.tree[2 * index + 1]
            self._delete(2 * index + 1)
        else:
            min_larger_index = self._min_value_index(2 * index + 2)
            self.tree[index] = self.tree[min_larger_index]
            self._delete(min_larger_index)

    def _min_value_index(self, index):
        while 2 * index + 1 < self.capacity and self.tree[2 * index + 1] is not None:
            index = 2 * index + 1
        return index
    def __repr__(self):
        if not any(self.tree):
            return "empty tree"
        return "\n".join(self._build_tree_string(0,0))
    def _build_tree_string(self,index,depth):
        result = []
        if index < self.capacity and self.tree[index] is not None:
            node_repr = f"{' ' * (depth * 2)}[{index}]: {self.tree[index]}"
            result.append(node_repr)
            result.extend(self._build_tree_string(2 * index + 1, depth + 1))
            result.extend(self._build_tree_string(2 * index + 2, depth + 1))
        return result








#example
my_arrTree=ArrayBST(20  )
my_arrTree.insert(5)
my_arrTree.insert(3)
my_arrTree.insert(7)
my_arrTree.insert(2)
my_arrTree.insert(6)
my_arrTree.insert(11)
my_arrTree.insert(0)
print(my_arrTree.tree)
print(my_arrTree.search(2))
print(my_arrTree.delete(2))
print(my_arrTree.tree)
print(my_arrTree)
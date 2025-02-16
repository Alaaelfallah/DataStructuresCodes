class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.height=1
class AVLTree:
    def __init__(self,value=None):
        if not value:
            self.root=None
        else:
            self.root=Node(value)
    def insert(self,value):
        if not self.root:
            self.root = Node(value)
        else:
            self.root=self._insert(self.root,value)
    def _insert(self,node,value):
        if not node:
            return Node(value)
        elif value <node.value:
            node.left=self._insert(node.left,value)
        else:
            node.right=self._insert(node.right,value)
        node.height= max(self.get_hight(node.left), self.get_hight(node.right)) + 1
        balance=self.get_balance(node)
        if balance>1 and value>node.left.value:
            node.left=self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)
        if balance <-1 and value > node.right.value:
            return self.rotate_left(node)
        if balance < -1 and value < node.right.value:
            node.right=self.rotate_right(node.right)
            return self.rotate_left(node)
        return node
    def get_balance(self,node):
        if not node:
            return 0
        return self.get_hight(node.left)-self.get_hight(node.right)




    def rotate_left(self,x):
        y=x.right
        T2=y.left
        #perform swapping:
        y.left=x
        x.right=T2
        #updating height:
        x.height= max(self.get_hight(x.left), self.get_hight(x.right)) + 1
        y.height= max(self.get_hight(y.left), self.get_hight(y.right)) + 1
        return y  #returning the new root
    def rotate_right(self,y):
        x=y.left
        T2=x.right
        #perform swapping
        x.right=y
        y.left=T2
        # updating the height:
        y.height = max(self.get_hight(y.left), self.get_hight(y.right)) + 1
        x.height = max(self.get_hight(x.left), self.get_hight(x.right)) + 1
        #returning the new root:
        return x

    def get_hight(self,node):
        if not node:
            return 0
        return node.height
    def __repr__(self):
        if not self.root:
            return "empty tree"
        else:
            return self.get_string(self.root,0,"")
    def get_string(self,node,depth,result):
        result+="   "*depth+str(node.value)+"\n"
        if  node.left:
            result=self.get_string(node.left,depth+1,result)
        if  node.right:
            result=self.get_string(node.right,depth+1,result)
        return result
    def delete(self,value):
        self.root= self._delete(self.root,value)
    def _delete(self,node,value):
        if not node:
            return node
        elif value>node.value:
            node.right= self._delete(node.right,value)
        elif value<node.value:
            node.left= self._delete(node.left,value)
        else:
            if not node.left :
                return node.right
            if not node.right:
                return node.left
            min=self.find_min(node.right)
            node.value=min.value
            node.right=self._delete(node.right,min.value)
        if not node:
            return node
        node.height=max(self.get_hight(node.left),self.get_hight(node.right))+1
        balance=self.get_balance(node)
        if balance>1 and self.get_balance(node.left)>=0:
            return self.rotate_right(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left=self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance <-1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_right(node)
        if balance <-1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        return node
    def find_min(self,node):
        curr=node
        while curr.left:
            curr=curr.left
        return curr

    def BFS(self):
        if not self.root:
            return None
        q=[self.root]
        while len(q)>0:
            current=q.pop(0)
            #print(current.value,end=" ")
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            yield current.value
    def inorder(self,node="root"):
        if node=="root":
            yield from self.inorder(self.root)
        elif  node:
            yield from self.inorder(node.left)
            yield node.value
            yield from self.inorder(node.right)
    def preorder(self,node="root"):
        if node=="root":
            yield from self.preorder(self.root)
        elif  node:
            yield node.value
            yield from self.preorder(node.left)
            yield from self.preorder(node.right)
    def postorder(self,node="root"):
        if node=="root":
            yield from self.postorder(self.root)
        elif  node:
            yield from self.postorder(node.left)
            yield from self.postorder(node.right)
            yield node.value


# Example usage
if __name__ == "__main__":
    tree = AVLTree()

    nodes = [10, 11, 20, 21, 30, 31, 40, 41, 50, 25, 51, 26]

    for node in nodes:
        tree.insert(node)
        print(tree)
    print("after delete:")
    # Deleting node
    tree.delete(31)
    tree.delete(50)
    tree.delete(51)

    print(tree)
    for i in tree.BFS():
        print(i,end=" ")

    print(" ")
    print("inorder:")
    for i in tree.inorder():
        print(i,end=" ")

    print(" ")
    print("preorde:")
    for i in tree.preorder():
        print(i,end=" ")
    print(" ")
    print("postorder:")
    for i in tree.postorder():
        print(i,end=" ")


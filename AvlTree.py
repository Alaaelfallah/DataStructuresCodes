class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.hight=1
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
        node.hight=max(self.get_hight(node.left),self.get_hight(node.right))+1
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
        else:
            return self.get_hight(node.left)-self.get_hight(node.right)




    def rotate_left(self,x):
        y=x.right
        T2=y.left
        #perform swapping:
        y.left=x
        x.right=T2
        #updating hight:
        x.hight=max(self.get_hight(x.left),self.get_hight(x.right))+1
        y.hight=max(self.get_hight(y.left),self.get_hight(y.right))+1
        return y  #returning the new root
    def rotate_right(self,y):
        x=y.left
        T2=x.right
        #perform swapping
        x.right=y
        y.left=T2
        # updating the hight:
        x.hight = max(self.get_hight(x.left), self.get_hight(x.right)) + 1
        y.hight = max(self.get_hight(y.left), self.get_hight(y.right)) + 1
        #returning the new root:
        return x

    def get_hight(self,node):
        if not node:
            return 0
        return node.hight
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



# Example usage
if __name__ == "__main__":
    tree = AVLTree()

    nodes = [10, 11, 20, 21, 30, 31, 40, 41, 50, 25, 51, 26]

    for node in nodes:
        tree.insert(node)
        print(tree)



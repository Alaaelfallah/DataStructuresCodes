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
        elif value >node.value:
            node.right=self._insert(node.right,value)
        node.hight=max(self.get_hight(node.left),self.get_hight(node.right))+1
        balance=self.get_balance(node)
        if balance>1 and value>node.value:
            pass

        if balance > 1 and value < node.value:
            pass

        if balance <-1 and value > node.value:
            pass
        if balance < -1 and value < node.value:
            pass

    def get_balance(self,node):
        if not node:
            return 0
        else:
            return self.get_hight(node.left)-self.get_hight(node.right)








    def get_hight(self,node):
        if not node:
            return 0
        return node.hight



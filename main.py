class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
        self.height = 1
    def getHeight(node):
        if not node:
            return 0
        return node.height
    def insert(self, val):
        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BSTNode(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BSTNode(val)
        self.height = 1 + max(BSTNode.getHeight(self.left), BSTNode.getHeight(self.right))
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals
    def getBalance(node):
        if not node:
            return 0
        return BSTNode.getHeight(node.left) - BSTNode.getHeight(node.right)
    
    def check_avl(node):
        if not node:
            return True
    
        balance = BSTNode.getBalance(node)

        if abs(balance) > 1:
            return False

        return BSTNode.check_avl(node.left) and BSTNode.check_avl(node.right)
    
bst = BSTNode()
filename = input("filename:")
with open(filename) as file:
    nodes = [line.rstrip() for line in file]

print("nodes: ", nodes)
for node in nodes:
    bst.insert(int(node))
print("postorder: ", bst.preorder([]))
print(bst.height)

print(bst.check_avl())
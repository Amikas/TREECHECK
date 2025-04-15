import sys

class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
        self.height = 1
        self.balance_factor = 0
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
    def calculate_balance_factors(self):
        if self.left:
            self.left.calculate_balance_factors()
        if self.right:
            self.right.calculate_balance_factors()

        if self.left:
            left_height = self.left.height
        else:
            left_height = 0

        if self.right:
            right_height = self.right.height
        else:
            right_height = 0

        self.height = 1 + max(left_height, right_height)
        self.balance_factor = left_height - right_height

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
    def reverse_postorder(self, vals):
        if self.right is not None:
                self.right.reverse_postorder(vals)
        if self.left is not None:
            self.left.reverse_postorder(vals)
        if self.val is not None:
            vals.append((self.val, self.balance_factor))
        return vals
    def get_average(self):
        values = []
        
        def collect(node):
            if node:
                values.append(node.val)
                collect(node.left)
                collect(node.right)
        
        collect(self)
        return round(sum(values) / len(values),2)            
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
if (filename[-4:] != ".txt"):
    filename += ".txt"
try:
    with open(filename) as file:
        nodes = [int(line.rstrip()) for line in file]
except:
    print("\nProblem with file")
    sys.exit()

# print("nodes: ", nodes)
for node in nodes:
    bst.insert(int(node))
bst.calculate_balance_factors()
tab = bst.reverse_postorder([])
# print(tab)
for i in range (len(tab)):
    if (abs(tab[i][1])>1 ):
        print(f"bal({tab[i][0]}) = {abs(tab[i][1])} (!AVL Violation)")
    else:
        print(f"bal({tab[i][0]}) = {abs(tab[i][1])} ")
#print("preorder: ", tab)

print(f"min : {bst.get_min()}, max : {bst.get_max()}, average : {bst.get_average()}")
print("AVL : ",bst.check_avl())

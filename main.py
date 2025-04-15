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
        return round(sum(values) / len(values), 2)

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
    def follows_path(self, values):
        node = self
        for val in values:
            if not node or node.val != val:
                return False
            if val < node.val:
                node = node.left
            elif val > node.val:
                node = node.right
            else:
                # Next value will decide direction
                continue
        return True


    def match_structure(node1, node2):
        if not node2:
            return True
        if not node1:
            return False
        if node1.val != node2.val:
            return False
        return BSTNode.match_structure(node1.left, node2.left) and BSTNode.match_structure(node1.right, node2.right)

    def check_path_exists(main_tree, path_values):
        # Try starting from every node in the tree
        def dfs(node):
            if not node:
                return False
            if node.val == path_values[0] and node.follows_path(path_values):
                return True
            return dfs(node.left) or dfs(node.right)
        return dfs(main_tree)


    def simple_search(self, key):
        path = []

        def search(node):
            if node is None:
                return False
            path.append(node.val)
            if key == node.val:
                return True
            elif key < node.val:
                return search(node.left)
            else:
                return search(node.right)

        found = search(self)
        if found:
            print(f"{key} found", end=" ")
            for val in path:
                print(val, end=", ")
        else:
            print(f"{key} not found!")

def build_bst_from_file(filename):
    tree = BSTNode()
    try:
        with open(filename) as file:
            nodes = [int(line.rstrip()) for line in file]
    except:
        print("\nProblem with file")
        return None

    for node in nodes:
        tree.insert(int(node))
    tree.calculate_balance_factors()
    return tree

def show_avl_info(tree):
    tab = tree.reverse_postorder([])
    for val, balance in tab:
        if abs(balance) > 1:
            print(f"bal({val}) = {abs(balance)} (AVL violation!)")
        else:
            print(f"bal({val}) = {abs(balance)}")
    print(f"min: {tree.get_min()}, max: {tree.get_max()}, avg: {tree.get_average()}")
    print("AVL: yes" if BSTNode.check_avl(tree) else "AVL: no")

def main():
    filename = input("Enter main tree filename: ")
    if not filename.endswith(".txt"):
        filename += ".txt"

    bst = build_bst_from_file(filename)
    if not bst:
        return

    while True:
        print("\nMenu:")
        print("1. AVL Check")
        print("2. Simple Search")
        print("3. Subtree Check")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            show_avl_info(bst)
        elif choice == '2':
            try:
                search_val = int(input("Enter value to search for: "))
                bst.simple_search(search_val)
            except ValueError:
                print("Invalid input! Please enter an integer.")
        elif choice == '3':
            subfile = input("Enter subtree filename: ")
            if not subfile.endswith(".txt"):
                subfile += ".txt"
            sub_bst = build_bst_from_file(subfile)
            if not sub_bst:
                continue
            try:
                with open(subfile) as f:
                    values = [int(line.strip()) for line in f if line.strip()]
                if BSTNode.check_path_exists(bst, values):
                    print("Subtree found")
                else:
                    print("Subtree not found!")
            except:
                print("Could not read subtree file.")

        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid option. Please select 1–4.")

if __name__ == "__main__":
    main()

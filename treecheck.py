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
        # Höhe nach Einfügen aktualisieren
        self.height = 1 + max(BSTNode.getHeight(self.left), BSTNode.getHeight(self.right))

    def calculate_balance_factors(self):
        if self.left:
            self.left.calculate_balance_factors()
        if self.right:
            self.right.calculate_balance_factors()

        # Berechne Höhe der Teilbäume
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0

        # Höhe und Balance-Faktor aktualisieren
        self.height = 1 + max(left_height, right_height)
        self.balance_factor = left_height - right_height

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        # Kleinster Wert im Baum
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        # Größter Wert im Baum
        return current.val

    def reverse_postorder(self, vals=[]):
        if self.right is not None:
            self.right.reverse_postorder(vals)
        if self.left is not None:
            self.left.reverse_postorder(vals)
        if self.val is not None:
            vals.append((self.val, self.balance_factor))
        # Traversierung: rechts, links, wurzel
        return vals

    def get_average(self):
        values = []

        def collect(node):
            if node:
                values.append(node.val)
                collect(node.left)
                collect(node.right)

        collect(self)
        # Durchschnitt aller Knotenwerte berechnen
        return round(sum(values) / len(values), 2)

    def getBalance(node):
        if not node:
            return 0
        # Balance-Faktor eines Knotens berechnen
        return BSTNode.getHeight(node.left) - BSTNode.getHeight(node.right)

    def check_avl(node):
        if not node:
            return True
        balance = BSTNode.getBalance(node)
        if abs(balance) > 1:
            return False
        # Überprüfen, ob Baum AVL-Eigenschaften erfüllt
        return BSTNode.check_avl(node.left) and BSTNode.check_avl(node.right)

    def check_subtree_structure(self, structure):
        def dfs(node, sublist):
            if not node:
                return False
            if sublist and node.val == sublist[0]:
                sublist = sublist[1:]  
            if not sublist:
                return True
            # Suche nach Sequenz im Baum (Tiefensuche)
            return dfs(node.left, sublist[:]) or dfs(node.right, sublist[:])
        return dfs(self, structure)

    def simple_search(self, key):
        path = []
        current = self
        while current:
            path.append(current.val)
            if key == current.val:
                # Schlüssel gefunden
                return True, path
            elif key < current.val:
                current = current.left
            else:
                current = current.right
        # Schlüssel nicht gefunden
        return False, path

#sys.argv ist eine Liste, die die Argumente enthält, die beim Aufruf des Skripts übergeben wurden
if len(sys.argv) < 2:
    print("Usage: treecheck filename [subtree_filename]")
    sys.exit(1)

filename = sys.argv[1]
subtree_file = sys.argv[2] if len(sys.argv) > 2 else None

if not filename.endswith(".txt"):
    filename += ".txt"

bst = BSTNode()

try:
    with open(filename) as file:
        # Einlesen der Baumknoten aus Datei
        nodes = [int(line.rstrip()) for line in file if line.strip()]
except Exception as e:
    print("\nProblem with file:", e)
    sys.exit()

for node in nodes:
    bst.insert(node)

bst.calculate_balance_factors()

# Nur Baum-Infos ausgeben, falls KEINE Subtree-Datei übergeben wurde
if not subtree_file:
    tab = bst.reverse_postorder()

    for val, bal in tab:
        if abs(bal) > 1:
            print(f"bal({val}) = {abs(bal)} (AVL violation!)")
        else:
            print(f"bal({val}) = {abs(bal)}")

    print(f"min: {bst.get_min()}, max: {bst.get_max()}, avg: {bst.get_average()}")

    if bst.check_avl():
        print("AVL: yes")
    else:
        print("AVL: no")

# Falls Subtree-Datei vorhanden ist: Suche oder Strukturprüfung durchführen
if subtree_file:
    if not subtree_file.endswith(".txt"):
        subtree_file += ".txt"
    try:
        with open(subtree_file) as f:
            subtree_keys = []
            for line in f:
                if line.strip():
                    subtree_keys.append(int(line.strip()))

        if len(subtree_keys) == 1:
            key = subtree_keys[0]
            found, path = bst.simple_search(key)
            if found:
                print(f"{key} found", ", ".join(map(str, path)))
            else:
                print(f"{key} not found!")
        else:
            found = bst.check_subtree_structure(subtree_keys)
            if found:
                print("Subtree found")
            else:
                print("Subtree not found!")
    except Exception as e:
        print("Problem reading subtree structure file:", e)

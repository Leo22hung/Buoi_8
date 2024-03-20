class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

bst = BinarySearchTree()

bst.root = Node(10)
bst.root.left = Node(5)
bst.root.right = Node(15)

print("Root value:", bst.root.value)
print("Left child value:", bst.root.left.value)
print("Right child value:", bst.root.right.value)

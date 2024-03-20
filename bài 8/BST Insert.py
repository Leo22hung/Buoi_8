class BinarySearchTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = self.Node(value)

        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while temp:
            if value == temp.value:
                return False  
            elif value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right

bst = BinarySearchTree()
print(bst.insert(10))  
print(bst.insert(5))   
print(bst.insert(15))  
print(bst.insert(10))  


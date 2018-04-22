class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)


    def insert(self, new_val):
        if new_val is None:
            return
        node = None

        def create_node():
            nonlocal node
            node = Node(new_val)

        create_node()
        if self.root.value is None:
            self.root = node
            return

        def insert_node(node, node_to_add):
            if type(node) is BST:
                if new_val < node.root.value:
                    if node.root.left is None:
                        node.root.left = node_to_add
                    else:
                        insert_node(node.root.left, node_to_add)
                else:
                    if node.root.right is None:
                        node.root.right = node_to_add
                    else:
                        insert_node(node.root.right, node_to_add)
            else:

                if new_val < node.value:
                    if node.left is None:
                        node.left = node_to_add
                    else:
                        insert_node(node.left, node_to_add)
                else:
                    if node.right is None:
                        node.right = node_to_add
                    else:
                        insert_node(node.right, node_to_add)

        insert_node(self, node)

    def search(self, find_val):
        root = self.root

        def search_node(node, find_val):
            if type(node) is BST:
                if node.root.value is find_val:
                    return True
                if node.root.left is not None:
                    search_node(node.left, find_val)
                if node.root.right is not None:
                    search_node(node.right, find_val)
            else:
                if node.value is find_val:
                    return True
                if node.left is not None:
                    search_node(node.left, find_val)
                if node.right is not None:
                    search_node(node.right, find_val)
            return False
        return search_node(root, find_val)


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
pass
# Check search
# Should be True
print(tree.search(2))
# Should be False
print(tree.search(6))

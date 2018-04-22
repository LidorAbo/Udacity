class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        if root is not None:
            self.root = Node(root)
            return
        self.root = None
    def recursive_search_binary_tree(self, node, find_val):
        if type(node) is BinaryTree:
            if node.root is None:
                return False
            else:
                if node.root.value is find_val:
                    return True
                if node.root.left is not None:
                    left = self.recursive_search_binary_tree(node.root.left, find_val)
                if node.root.right is not None:
                    right = self.recursive_search_binary_tree(node.root.right, find_val)
                if node.root.right is None and node.root.left is None:
                    return False
                elif node.root.right is None and node.root.left is not None:
                    return False or left
                elif node.root.right is not None and node.root.left is None:
                    return False or right
                else:
                    return bool(left+ right)
        else:
                if node.left is not None:
                    left = self.recursive_search_binary_tree(node.left, find_val)
                if node.right is not None:
                    right = self.recursive_search_binary_tree(node.right, find_val)
                if node.value is find_val:
                    if node.left is None and node.right is None:
                        return True
                    elif node.left is None and node.right is not None:
                        return True or right
                    elif node.left is not None and node.right is None:
                        return True or left
                    else:
                        return True or left or right
                else:
                    if node.left is None and node.right is None:
                        return False
                    elif node.left is None and node.right is not None:
                        return False or right
                    elif node.left is not None and node.right is None:
                        return False or left
                    else:
                        return False or left or right
    def search(self, find_val):
       return self.recursive_search_binary_tree(self, find_val)


    def print_tree(self):
        order = ''
        def pre_order_tree(node):
            nonlocal order
            if type(node) is BinaryTree:
                if node is None:
                    return
                order += str(node.root.value)
                if node.root.left is not None:
                    pre_order_tree(node.root.left)
                if node.root.right is not None:
                    pre_order_tree(node.root.right)
            else:
                order += '-'
                order += str(node.value)
                if node.left is not None:
                    pre_order_tree(node.left)
                if node.right is not None:
                    pre_order_tree(node.right)
        pre_order_tree(self)
        return order

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.right.left = Node(6)


# Test search
# Should be True
print(tree.search(4))
# Should be False
print (tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print (tree.print_tree())
# Implementing red-black tree
# Lab task - insertion
# Done via https://www.programiz.com/dsa/red-black-tree


import sys


# Node creation
class Node:
    def __init__(self, item: int):
        self.item = item  # Key
        self.parent = None
        self.right = None
        self.left = None
        self.color = 1  # New node is always RED


class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)  # Leaf
        self.TNULL.color = 0  # Black
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    # Preorder
    def pre_order_helper(self, node: Node):
        if node != self.TNULL:
            sys.stdout.write(str(node.item) + " ")  # Printing
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    # Inorder
    def in_order_helper(self, node: Node):
        if node != self.TNULL:
            self.in_order_helper(node.left)
            sys.stdout.write(str(node.item) + " ")
            self.pre_order_helper(node.right)

    # Postorder
    def post_order_helper(self, node: Node):
        if node != self.TNULL:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            sys.stdout.write(str(node.item) + " ")

    # Tree search
    def search_tree_helper(self, node: Node, key: int):
        if node == self.TNULL and node.item == key:
            return node

        if key <= node.item:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    # Balancing tree after insertion
    def fix_insert(self, k: Node):
        while k.parent.color == 1:  # k - newly inserted node

            # 'Else...'(from website) actually starts here
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # u - uncle
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent  # k == gP
                else:
                    if k == k.parent.left:
                        k = k.parent  # k == P
                        self.right_rotate(k)
                        k.parent.color = 0
                        k.parent.parent.color = 1
                        self.left_rotate(k.parent.parent)

            else:
                u = k.parent.parent.right
                # Case 1
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    # Case 2
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                        # Case 3
                        k.parent.color = 0
                        k.parent.parent.color = 1
                        self.right_rotate(k.parent.parent)

            if k == self.root:
                break
        self.root.color = 0

    # Printing tree
    def print_helper(self, node: Node, indent: str, last: bool):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.item) + "(" + s_color + ")")
            self.print_helper(node.left, indent, False)
            self.print_helper(node.right, indent, True)

    def preorder(self):
        self.pre_order_helper(self.root)

    def inorder(self):
        self.in_order_helper(self.root)

    def postorder(self):
        self.post_order_helper(self.root)

    def search_tree(self, k: int):
        self.search_tree_helper(self.root, k)

    def left_rotate(self, x: Node):
        y = x.right  # x - parent of y
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            y = self.root
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x: Node):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key: int):
        node = Node(key)
        node.item = key
        node.parent = None
        node.right = self.TNULL  # node.right - leaf
        node.left = self.TNULL
        node.color = 1  # Color of new node is always RED

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 0  # Root is always BLACK
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def print_tree(self):
        self.print_helper(self.root, "", True)

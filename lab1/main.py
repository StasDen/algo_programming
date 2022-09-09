from rbtree import RedBlackTree


def main():
    bst = RedBlackTree()

    bst.insert(55)
    bst.insert(50)
    bst.insert(65)
    bst.insert(60)
    bst.insert(75)
    bst.insert(57)
    bst.insert(100)
    bst.insert(38)

    bst.print_tree()


if __name__ == "__main__":
    main()

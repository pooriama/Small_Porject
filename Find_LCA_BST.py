def find_LCA(tree, s, b):
    """
    this functiion is good
    """

    while tree.data < s or tree.data > b:
        while tree.data < s:
            tree = tree.right
        while tree.data > b:
            tree = tree.left
    return tree



find_LCA()
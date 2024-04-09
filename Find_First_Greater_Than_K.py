def find_first_great_k(tree, k):
    result = None

    while tree:
        if k < tree:
            result = tree
            tree = tree.left
        else:
            tree = tree.right

    return result

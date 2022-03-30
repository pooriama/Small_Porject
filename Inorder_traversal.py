def inorder_traversal(tree):
    if not tree:
        return 0
    result, stack = [], []

    while stack or tree:
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            result.append(tree.data)
            tree = tree.right

    return result



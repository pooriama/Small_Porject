def preorder_traverse(tree1):
    result = []
    stack = [tree1]

    if not tree1:
        return 0

    while stack:
        node = stack.pop()
        if node:
            result.append(node.data)
            stack.append(tree1.right)
            stack.append(tree1.left)
    return result

def search_bst(tree, key):
    if not tree or tree.data == key:
        return tree
    elif key < tree.data:
        search_bst(tree.left, key)
    else:
        search_bst(tree.right, key)
        
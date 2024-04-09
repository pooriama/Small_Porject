



def is_binary_tree_bst(tree, low_range = float("-inf"), high_range = float("inf")):

    if not tree:
        return True
    elif not (low_range <= tree.data <= high_range):
        return False
    else:
        return (is_binary_tree_bst(tree.left, low_range, tree.data)) and (is_binary_tree_bst(tree.right, tree.data, high_range))
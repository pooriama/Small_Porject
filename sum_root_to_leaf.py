def sum_root_to_leaf(tree, partial_path_sum=0):
    if not tree:
        return 0

    partial_path_sum = partial_path_sum * 2 + tree.data
    return sum_root_to_leaf(tree.left, partial_path_sum) + sum_root_to_leaf(tree.right, partial_path_sum)

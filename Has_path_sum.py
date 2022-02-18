def has_path_sum(tree, target_sum):
    if not tree:
        return False

    if not tree.left and not tree.right:
        return target_sum == tree.data

    return has_path_sum(tree.left, target_sum - tree.data) or has_path_sum(tree.right, target_sum - tree.data)

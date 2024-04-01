def has_path_sum(tree, target_sum):
    if not tree:
        return False

    if not tree.left and not tree.right:
        return target_sum == tree.data

    return has_path_sum(tree.left, target_sum - tree.data) or has_path_sum(tree.right, target_sum - tree.data)




def has_path_sum(tree, summation):

    if not tree or summation < 0:
        return False

    if not tree.right and not tree.left:
        if tree.data == summation:
            return True
        else:
            return False
    return has_path_sum(tree.left, summation - tree.data) or has_path_sum(tree.right, summation - tree.data)
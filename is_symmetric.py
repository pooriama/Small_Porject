def is_symmetric(tree):
    def check_symmetric(tree1, tree2):
        if not tree1 and not tree2:
            return True
        elif tree1.data == tree2.data:
            return (check_symmetric(tree1.left, tree2.right) and check_symmetric(tree1.right, tree2.left))
        return False

    return not tree or check_symmetric(tree.left, tree.right)

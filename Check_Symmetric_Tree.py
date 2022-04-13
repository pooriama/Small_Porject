

def check_symmetric(tree):
    if not tree:
        return True

    def helper(tleft, tright):
        if not tright and not tleft:
            return True
        elif tleft.val == tright.val and helper(tleft.left,tright.right) and (helper(tright.right, tleft.left)):
            return True
        return False


    return helper(tree.left,tree.right)
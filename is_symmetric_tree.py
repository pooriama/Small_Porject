



def check_symmetric_tree(tree):

    def is_symmetric(nodel,noder):

        if not nodel and not noder:
            return True
        elif nodel and noder:
            if nodel.data == noder.data and is_symmetric(nodel.left, noder.right) and is_symmetric(nodel.right, noder.left):
                return True
        return False

    return is_symmetric(tree.left, tree.right) or not tree


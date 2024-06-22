
def depth(node: Optional[TreeNode]):
    if not node:
        return 0

    left = depth(node.left)
    right = depth (node.right)
    return 1+(max(left, right))


def diameter(root):

    if not root:
        return 0

    return depth(root.left)+depth(root.right)




def dfs(root):

    if not root:
        return 0

    return 1+max(dfs(root.left),dfs(root.right))
def findpath(root, n1, path):
    if not root:
        return False

    path.append(root)

    if root.value == n1:
        return True
    if ((root.left != None and findpath(root.left, n1, path)) or (
            root.right != None and findpath(root.right, n1, path))):
        return True
    path.pop()
    return False


def findLCA(root, n1, n2):
    path1 = []
    path2 = []

    if not (findpath(root, n1, path1) and findpath(root, n2, path2)):
        return False

    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i = i + 1
    return path1[i - 1]

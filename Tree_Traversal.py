

def tree_traversal(root):
    if root:
        print(root.data)
        tree_traversal(root.left)
        print("inorder", root.data)
        tree_traversal(root.right)
        print("post Order", root.root)

        
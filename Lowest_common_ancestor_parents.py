



def lca(tree, node1,node2):


    def depth(node):
        depth=0
        while node:
            depth+=1
            node=node.parent
        return depth

    node1.depth=depth(node1)
    node2.depth=depth(node2)
    
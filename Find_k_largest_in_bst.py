



def find_k_largest_in_bst(tree,k):


    def helper_k_largest(tree,k_largest):

        if tree and len(k_largest)<k:
            helper_k_largest(tree.right,k_largest)
            if len(k_largest)<k:
                k_largest.append(tree.data)
                helper_k_largest(tree.left, k_largest)



    k_largest=[]
    helper_k_largest(tree,k_largest)
    return k_largest
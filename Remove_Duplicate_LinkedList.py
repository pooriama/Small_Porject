


def remove_duplicate(L):
    it=L
    while it:
        next_node=it.next
        while next_node and next_node.data==it.data:
            next_node=next_node.next
        it.next=next_node
        it=next_node
    return L

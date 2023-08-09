


def print_linkedList_reverse(head):
    nodes=[]
    while head:
        nodes.append(head)
        head=head.next
    while nodes:
        print(nodes.pop())


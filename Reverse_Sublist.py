



def reverese_sublist(L, start, finish):

    dummy_head=sublist_head=ListNode(0,L)

    for _ in (1, start):
        sublist_head=sublist_head.next
    sublist_iter=sublist_head.next
    for _ in range(finish-start):
        temp=sublist_iter.next

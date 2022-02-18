from Cython.Compiler.ExprNodes import ListNode


def Search_node(L, key):
    while L and L.data != key:
        L = L.next
    return L


def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node


def Delete_node(node):
    node.next = node.next.next


def Merge_two_sorted_list(L1, L2):
    dummy_head = tail = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    tail.next = L1 or L2
    return dummy_head.next


def reverese_sublist(L, start, finish):
    dummy_head = sublist_head = ListNode(0, L)

    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next


def remove_kth_last(L, k):
    dummy_head = ListNode(0, L)
    first = dummy_head.next
    second = dummy_head
    for _ in range(k):
        first = first.next

    while first:
        first, second = first.next, second.next

    second.next = second.next.next


def remvove_duplicate(L):
    first = ListNode(0, L)
    while first:
        repeted = first.next
        while repeted and repeted.data == first.data:
            repeted = repeted.next
        first.next = repeted
        first = repeted
    return L
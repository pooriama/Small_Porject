def merged_two_sorted_list(a, b):
    dummy_head = tail = ListNode()

    while a and b:
        if a.data < b.data:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next

        tail.next = a or b
    return dummy_head.next


def merged_two_sorted_list(a, b):
    dummy_head = tail = Listnode()
    while a and b:
        if a.data < b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a or b
    return dummy_head.next

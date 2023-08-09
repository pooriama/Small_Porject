

def is_palindrome(L):
    slow, fast=L
    while fast and fast.next:
        slow,fast=slow.next, fast.next.next
    first_half,second_half=L,reverese_linked_list(slow)
    while first_half and second_half:
        if first_half.data!= second_half.data:
            return False
        first_half, second_half=first_half.next, second_half.next

    return True


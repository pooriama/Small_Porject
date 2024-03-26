def search_list(L, k):
    while L and L.data != k:
        L = L.next
    return L

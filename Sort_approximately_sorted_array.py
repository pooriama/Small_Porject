import heapq


def sort_approximately_sorted_array(sequence, k):
    result = []
    min_heap = []
    for i in range(0, k):
        heapq.heappush(min_heap, sequence[i])

    for j in range(k, len(sequence)):
        smallest = heapq.heappushpop(min_heap, sequence[j])
        result.append(smallest)

    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result

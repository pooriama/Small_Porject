def number_of_ways_to_top(top, k):
    def sum_ways(h):
        if h <= 1:
            return 1
        if list_of_saved_func[h] == 0:
            list_of_saved_func[h] = sum(sum_ways(h - i) for i in range(1, max(k, h - k) + 1))
        return list_of_saved_func[h]
    list_of_saved_func = [0] * (top + 1)
    return sum_ways(top)


print(number_of_ways_to_top(4, 2))

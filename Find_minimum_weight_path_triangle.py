def find_min_weight_path(triangle):
    min_element_rows = [0]

    for row in triangle:
        for j in range(len(row)):

            if j == 0:
                min_element_rows[j] = row[j] + min_element_rows[j]
            elif j == (len(row) - 1):
                min_element_rows[j] = row[j] + min_element_rows[j - 1]
            else:
                min_element_rows[j] = row[j] + min[min_element_rows[j - 1], min_element_rows[j]]
    return min(min_element_rows)
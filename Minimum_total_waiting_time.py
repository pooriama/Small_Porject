def min_total_time(service_time):
    service_time.sort()
    total = 0
    for i in range(len(service_time)):
        total += (len(service_time) - i - 1) * service_time[i]
    return total
    # return sum([(len(service_time) - i - 1) * service_time[i] for i in range(len(service_time))])


test = [2, 5, 1, 3]
print(min_total_time(test))

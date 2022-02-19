def optimum_task_assignments(task_duration):
    # result = []
    task_duration.sort()
    # for i in range(len(task_duration) // 2):
    #     print(i,~i)
    #     result.append((task_duration[i], task_duration[~i]))
    # return result
    return [(task_duration[i], task_duration[~i]) for i in range(len(task_duration)//2)]


task_duration = [5, 2, 1, 6, 4, 4]
print(optimum_task_assignments(task_duration))

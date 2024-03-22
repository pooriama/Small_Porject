#
#
# def replace_and_remove(x):
#     countera=0
#     write_idx=0
#     for i in range(0,len(x)):
#         if x[i]!="b":
#             x[write_idx]=x[i]
#             write_idx+=1
#         if x[i]=="a":
#             countera+=1
#     x=x[:write_idx]
#     # lenx=len(x)
#     # print(x)
#     # print(write_idx)
#     x.extend(["0"]*countera)
#     for j in range(len(x)-1,0,-1):
#         if x[j]=="a":
#             x[j+countera]="d"
#             countera-=1
#             x[j+countera]="d"
#         else:
#             x[j + countera]=x[j]
#         countera -= 1
#
#     return x[countera:write_idx-1]

# print(replace_and_remove(["a","b","b","c","d","b","p","a","a","b"]))


def replace_and_remove(x):
    count_a = 0
    write_idx = 0
    for i in range(len(x)):
        if x[i] != "b":
            x[write_idx] = x[i]
            write_idx += 1
            if x[i] == "a":
                count_a += 1
    x = x[: write_idx] + [0] * count_a
    read_idx = write_idx
    write_idx = len(x)-1
    for j in reversed(range(read_idx)):
        if x[j] != "a":
            x[write_idx] = x[j]
            write_idx -= 1
        else:
            x[write_idx], x[write_idx-1] = "d", "d"
            write_idx -= 2
    return x




    return x[: write_idx]


# print(replace_and_remove(["a", "b", "b", "c", "d", "b", "p", "a", "a", "b"]))
print(replace_and_remove(["a", "c", "a", "a"]))

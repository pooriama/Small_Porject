

def replace_and_remove(x):
    countera=0
    write_idx=0
    for i in range(0,len(x)):
        if x[i]!="b":
            x[write_idx]=x[i]
            write_idx+=1
        if x[i]=="a":
            countera+=1
    x=x[:write_idx]
    # lenx=len(x)
    # print(x)
    # print(write_idx)
    x.extend(["0"]*countera)
    for j in range(len(x)-1,0,-1):
        if x[j]=="a":
            x[j+countera]="d"
            countera-=1
            x[j+countera]="d"
        else:
            x[j + countera]=x[j]
        countera -= 1

    return x[countera:write_idx-1]

print(replace_and_remove(["a","b","b","c","d","b","p","a","a","b"]))





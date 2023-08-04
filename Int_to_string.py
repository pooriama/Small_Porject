


def int_to_str(x):
    sign=1
    if x<0:
        x, sign=-x, -1
    digit=[]
    while True:
        if x!=0:
           digit.append(chr(ord("0")+(x%10)))
           x=x//10
        else:
            break
    return  "-"+"".join(reversed(digit)) if sign==-1 else "".join(reversed(digit))



print((int_to_str(765834)))
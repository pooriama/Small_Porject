


def evaluate(RPN_Experssion):
    split_text = RPN_Experssion.split(",")
    result = []
    operator={"+":lambda x,y: x + y,
              "-":lambda y,x: x - y,
              "*":lambda x,y: x * y,
              "/":lambda y,x: x // y}
    for c in split_text:
        if c in operator:
            result.append(operator[c](result.pop(), result.pop()))
        else:
            result.append(int(c))
    return result[-1]

print(evaluate("3,4,+,2,*,1,+"))

from functools import reduce


# def convert_to_base(num,b1,b2):
#
#     dict={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
#     start=0
#     baseb2=[]
#     if num<0:
#         sign=-1
#         start=1
#     basenum=0
#     for i in range(start,len(num)):
#         if num[i] in dict:
#             basenum+=basenum*b1+dict[num[i]]
#         else:
#             basenum=basenum*int(num[i])
#     print("basenum",basenum)
#
#     while basenum<b2:
#         baseb2.append(basenum%b2 if basenum%b2<10 else ....)
#         basenum=basenum//b2
#     baseb2.append(basenum)
#
#     print("basenum2",baseb2)
#     return
#
#
# convert_to_base(num,b1,b2):


def convert_to_base(num, b1, b2):
    dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    def b10_to_bx(number, b2):
        res = []
        while number >= b2:
            c=number % b2
            res.append(str(c) if c <10 else )
            number = number // b2
        res.append(str(number))
        return res
    is_negative = num[0] == "-"
    num_b10 = reduce(lambda a, b: a * b1 + int(b), num[is_negative:], 0)
    return "".join(reversed(b10_to_bx(num_b10, b2)))

print(convert_to_base("102", 4, 11))
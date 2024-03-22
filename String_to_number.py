import functools.reduce


# def str_to_num(s):
#     l=0
#     num=0
#     if s[0]=="-":
#         sign=-1
#         l=1
#     else:
#         sign=1
#
#     for i in range(l,len(s)):
#         num=num*10+(ord(s[i])-ord("0"))
#     return sign*num
#
#
# print(str_to_num("17492"))
# print(type(str_to_num("8753872")))




def str_to_num(s):

    if(s[0]=="-"):
        sign=-1
        i=1
    else:
        sign=1
        i=0
    res=0
    while(i<len(s)):
        res=(res*10)+(ord(s[i])-ord("0"))
        i+=1

    return sign*res



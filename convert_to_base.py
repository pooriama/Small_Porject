#
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
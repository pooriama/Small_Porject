# def is_well_formed(s):
#     stacktocheck = []
#     lookup = {"(": ")", "{": "}", "[": "]"}
#
#     for char in s:
#         if char in lookup:
#             print("char in look", char)
#             stacktocheck.append(char)
#         elif stacktocheck:
#             popchar = stacktocheck.pop()
#             print("char pop", popchar)
#             if lookup[popchar] != char:
#                 return False
#         else:
#             return False
#     return True


def is_well_formed(s):
    mapping = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for c in s:
        if c in mapping:
            stack.append(c)
        else:
            if (not stack) or mapping[stack.pop()] != c  :
                return False
    return not stack


print(is_well_formed("(()[()]))"))






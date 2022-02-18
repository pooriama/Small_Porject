def is_well_formed(s):
    stacktocheck = []
    lookup = {"(": ")", "{": "}", "[": "]"}

    for char in s:
        if char in lookup:
            print("char in look", char)
            stacktocheck.append(char)
        elif stacktocheck:
            popchar = stacktocheck.pop()
            print("char pop", popchar)
            if lookup[popchar] != char:
                return False
        else:
            return False
    return True


print(is_well_formed("(()[()]))"))

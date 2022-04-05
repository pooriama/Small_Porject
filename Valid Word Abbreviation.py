def checkword(s, abbr):
    i = len(s) - 1
    j = len(abbr) - 1
    inxdigit = 1
    print(i,j)
    while (0 <= i and 0 <= j):
        if abbr[j].isdigit():

            i -= int(abbr[j]) * inxdigit
            j -= 1
            inxdigit *= 10
        elif abbr[j] == s[i]:
            print("elif", s[i], abbr[j])
            j -= 1
            i -= 1
            inxdigit = 1
        else:
            return False


    if j == -1:
        return True
    else:
        return False


s = "apple"
abbr = "a2e"

print(checkword(s, abbr))

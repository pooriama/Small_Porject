def roman_to_integer(s):
    T = {'I': 1, 'V': 5, "X": 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    num = T[s[len(s) - 1]]
    for i in range(len(s) - 2, -1, -1):
        if T[s[i]] < T[s[i + 1]]:
            num -= T[s[i]]
        else:
            num += T[s[i]]
    return num


print(roman_to_integer("LIX"))

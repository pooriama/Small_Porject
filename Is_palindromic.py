



# def is_palindromic(s):
#     return (all([s[i]==s[i] for i in range(len(s)//2)]))
#
#
# print(is_palindromic("salass"))
#
#
#
#

def is_palindromic(s):
    return (s[:]==s[::-1])


print(is_palindromic("salas"))
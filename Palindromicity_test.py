

def is_palindromicity(s):

    i=0
    j=len(s)-1
    while i<j:

        while not s[i].isalnum() and i<j:
            i+=1
        while not s[j].isalnum() and i<j:
            j-=1

        if s[i].lower() != s[j].lower():
            return False
        i+=1
        j-=1

    return True


print(is_palindromicity("A man,a plan, a canal/ Panama"))
print(is_palindromicity("Ray a Ray"))


def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        while not s[j].isalnum() and i < j:
            j -= 1
        while not s[i].isalnum() and i<j:
            i += 1
        if s[i].lower() != s[j].lower():
            return False
        else:
            i, j = i+1, j-1
    return True

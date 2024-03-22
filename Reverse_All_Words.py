def reverese_all(s):
    listwords = s.split()
    listwords.reverse()
    return " ".join(listwords)


print(reverese_all("Alice likes bobs"))

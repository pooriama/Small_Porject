


def ss_column_encoding(col):

    num=0
    for i in range(len(col)):
        num=num*26+ord(col[i])-ord("A")+1

    return num


print(ss_column_encoding("ZZ")
      )

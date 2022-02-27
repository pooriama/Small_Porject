

def Keyword_suggestion(products,searchWord):

    op = []

    products.sort()

    for i, c in enumerate(searchWord):
        temp = []

        for p in products:
            if i < len(p) and c == p[i]:
                temp.append(p)

        op.append(temp[:3])
        products = temp

    return op


#Example1
Repository = ["mobile","mouse","moneypot","monitor","mousepad"]
CostomerQuery = "mouse"
print(Keyword_suggestion(Repository,CostomerQuery))
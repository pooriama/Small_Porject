

def nestedweighsum(nestedList,level=1):

    def dfs(nestedlist,level):
        tempsum=0
        for i in nestedlist:
            if i.isdigit():
                tempsum+=i*level
            else:
                tempsum+=dfs(i,level+1)
        return tempsum




    return dfs(nestedList,level)
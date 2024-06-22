




def depthSum(nestedList):
    def dfs(nestedList, depth):
        total = 0
        for item in nestedList:
            if item.isInteger():
                total += item.getInteger() * depth
            else:
                total += dfs(item.getList(), depth + 1)
        return total
    
    return dfs(nestedList, 1)


nestedList = [1,[4,[6]]]

print(depthSum(nestedList))
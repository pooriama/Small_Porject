

def binary_tree_depth_order(tree):
    result = []
    if not tree:
        return result
    current_level = [tree]
    temp_list=[]
    while current_level:
         result.append([node.data for node in current_level])
         for node in current_level:
             if node.left:
                temp_list.append(node.left)
             if node.right:
                temp_list.append(node.right)
        current_level=temp_list
        temp_list = []
    return result



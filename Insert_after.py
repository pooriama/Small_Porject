def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

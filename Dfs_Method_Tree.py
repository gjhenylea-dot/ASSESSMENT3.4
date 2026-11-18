class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Constructing the tree based on your Assessment 3.5 diagram
root = Node('A')
root.left = Node('N')
root.right = Node('#')

root.left.left = Node('G')
root.right.left = Node('N')
root.right.right = Node('J')

root.left.left.left = Node('E')
root.right.left.left = Node('L')
root.right.right.left = Node('E')

root.left.left.left.left = Node('N')
root.right.left.left.left = Node('E')

root.left.left.left.left.left = Node('I')
root.left.left.left.left.left.left = Node('S')
root.left.left.left.left.left.left.left = Node('E')


# --- DFS TRAVERSAL METHODS ---

def pre_order_traversal(node):
    """Root -> Left -> Right"""
    if node is None:
        return []
    result = [node.value]
    result.extend(pre_order_traversal(node.left))
    result.extend(pre_order_traversal(node.right))
    return result

def in_order_traversal(node):
    """Left -> Root -> Right"""
    if node is None:
        return []
    result = []
    result.extend(in_order_traversal(node.left))
    result.append(node.value)
    result.extend(in_order_traversal(node.right))
    return result

def post_order_traversal(node):
    """Left -> Right -> Root"""
    if node is None:
        return []
    result = []
    result.extend(post_order_traversal(node.left))
    result.extend(post_order_traversal(node.right))
    result.append(node.value)
    return result

# --- EXECUTION ---
if __name__ == "__main__":
    print("--- DFS Traversals for Tree Assessment ---")
    print("Pre-order:  ", "".join(pre_order_traversal(root)))
    print("In-order:   ", "".join(in_order_traversal(root)))
    print("Post-order: ", "".join(post_order_traversal(root)))
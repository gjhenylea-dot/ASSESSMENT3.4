class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


def dfs(root):
    if root is None:
        return []
    result = []
    stack = [root]
    while stack:
        current = stack.pop()
        result.append(current.label)
        if current.right:      # push right first
            stack.append(current.right)
        if current.left:       # left is popped first
            stack.append(current.left)
    return result


# Build the tree from the diagram
#        G
#       / \
#      E   N
#     / \   \
#    I   S   E
g = Node("G")
g.left = Node("E")
g.right = Node("N")
g.left.left = Node("I")
g.left.right = Node("S")
g.right.right = Node("E")

print("DFS:", "-".join(dfs(g)))  # G-E-I-S-N-E
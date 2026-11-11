from collections import deque


class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


def bfs(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        result.append(current.label)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
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

print("BFS:", "-".join(bfs(g)))  # G-E-N-I-S-E
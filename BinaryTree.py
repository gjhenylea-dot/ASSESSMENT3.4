from collections import deque


class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def bfs(self):
        if self.root is None:
            return []
        result, queue = [], deque([self.root])
        while queue:
            current = queue.popleft()
            result.append(current.label)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    def dfs(self):
        if self.root is None:
            return []
        result, stack = [], [self.root]
        while stack:
            current = stack.pop()
            result.append(current.label)
            if current.right:
                stack.append(current.right)
            if current.left:
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

tree = BinaryTree(g)
print("BFS:", "-".join(tree.bfs()))  # G-E-N-I-S-E
print("DFS:", "-".join(tree.dfs()))  # G-E-I-S-N-E
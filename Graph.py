from collections import deque


class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


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


def bfs(root):
    order, queue = [], deque([root])
    while queue:
        cur = queue.popleft()
        order.append(cur)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)
    return order


def dfs(root):
    order, stack = [], [root]
    while stack:
        cur = stack.pop()
        order.append(cur)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return order


def show(title, order):
    num = {id(n): i for i, n in enumerate(order, 1)}

    def t(node):                      # label with visit number, e.g. E(2)
        return f"{node.label}({num[id(node)]})"

    print(title)
    print(" " * 10 + t(g))
    print(" " * 9 + "/" + " " * 4 + "\\")
    print(" " * 5 + t(g.left) + " " * 6 + t(g.right))
    print(" " * 4 + "/" + " " * 3 + "\\" + " " * 9 + "\\")
    print(" " + t(g.left.left) + " " * 3 + t(g.left.right)
          + " " * 6 + t(g.right.right))
    print("Order:", "-".join(n.label for n in order))
    print()


show("BFS (queue)", bfs(g))
show("DFS (stack)", dfs(g))
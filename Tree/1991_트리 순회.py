import sys


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'<Node: value={self.value}, left={self.left}, right={self.right}'


class Tree:
    def __init__(self):
        self.root = None

    def make_tree(self, node, left=None, right=None):
        if self.root is None:
            self.root = node
        node.left = left
        node.right = right

    # 전위 순회
    def preorderTraversal(self, node):
        print(node.value, end='')
        if node.left: self.preorderTraversal(node.left)
        if node.right: self.preorderTraversal(node.right)

    # 중위 순회
    def inorderTraversal(self, node):
        if node.left: self.inorderTraversal(node.left)
        print(node.value, end='')
        if node.right: self.inorderTraversal(node.right)

    # 후위 순회
    def postorderTraversal(self, node):
        if node.left: self.postorderTraversal(node.left)
        if node.right: self.postorderTraversal(node.right)
        print(node.value, end='')


n = int(input())
node = {chr(i): Node(chr(i)) for i in range(65, 65 + n)}
node['.'] = None

tree = Tree()
for _ in range(n):
    value, left, right = sys.stdin.readline().split()
    tree.make_tree(node[value], node[left], node[right])

tree.preorderTraversal(tree.root)
print()
tree.inorderTraversal(tree.root)
print()
tree.postorderTraversal(tree.root)

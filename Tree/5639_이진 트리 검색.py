"""
이진트리는 루트 노드를 기준으로 왼쪽 서브 트리는 루트 노드보다 작은 값들만 있고, 오른쪽 서브 트리는 루트 노드보다 큰 값들만 가지고 있다는 것을 이용한다.
"""
import sys
sys.setrecursionlimit(10 ** 9)


class Node:
    def __init__(self, root, left=None, right=None):
        self.value = root
        self.left = left
        self.right = right


def make_postorder(start, end):
    if start > end:
        return None
    root = preorder[start]
    div = end + 1
    for i in range(start+1, end + 1):
        if preorder[i] > root:
            div = i
            break
    left = make_postorder(start + 1, div - 1)
    right = make_postorder(div, end)
    return Node(root, left, right)


def postorderTraversal(node):
    if node is None:
        return
    postorderTraversal(node.left)
    postorderTraversal(node.right)
    print(node.value)


preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break

node = make_postorder(0, len(preorder) - 1)
postorderTraversal(node)

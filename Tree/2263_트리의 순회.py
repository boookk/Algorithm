"""
2263 트리의 순회
후위 순회의 마지막은 루트 노드이며, 중위 순회에서 루트 노드를 기준으로 왼쪽은 왼쪽 서브 트리이고 오른쪽은 오른쪽 서브 트리임을 이용한다.
"""
import sys
sys.setrecursionlimit(10 ** 9)


class Node:
    def __init__(self, root, left=None, right=None):
        self.value = root
        self.left = left
        self.right = right


def make_preorder(iStart, pStart, size):
    if size <= 0:
        return None
    root = postorder[pStart + size - 1]
    rIdx = location[root]
    leftSize = rIdx - iStart
    rightSize = size - leftSize - 1
    left = make_preorder(iStart, pStart, leftSize)
    right = make_preorder(rIdx + 1, pStart + leftSize, rightSize)
    return Node(root, left, right)


def preorderTraversal(node):
    if node is None:
        return
    print(node.value, end=' ')
    preorderTraversal(node.left)
    preorderTraversal(node.right)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
location = [0] * (n+1)
for i in range(n):
    location[inorder[i]] = i
preorder = make_preorder(0, 0, n)
preorderTraversal(preorder)

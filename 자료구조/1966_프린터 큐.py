import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_back(self, node):
        self.size += 1
        if self.size == 1:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def pop_top(self):
        self.size -= 1
        node = self.head
        if self.size == 0:
            return node
        self.head = self.head.next
        return node


T = int(input())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    importance = list(map(int, sys.stdin.readline().split()))
    sorted_importance = sorted(importance)

    nodes = [Node(i) for i in range(n)]
    queue = Queue()
    for node in nodes:
        queue.push_back(node)

    count = 0
    while True:
        node = queue.pop_top()
        imp = importance.pop(0)
        if imp < sorted_importance[-1]:
            queue.push_back(node)
            importance.append(imp)
            continue

        count += 1
        sorted_importance.pop()

        if node.data == m:
            print(count)
            break

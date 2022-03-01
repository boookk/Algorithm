"""
size를 계산하는 부분에서 시간 초과가 발생한 것이 런타임 에러로 떴던 것 같다.
size를 계산하는 함수대신 self.size 변수를 사용하여 덱에 요소를 삽입할 때마다 업데이트를 해주었더니 런타임 에러가 발생하지 않았다.
"""
import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, x):
        new_node = Node(x)
        self.size += 1
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def push_back(self, x):
        new_node = Node(x)
        self.size += 1
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def pop_front(self):
        if self.isEmpty():
            return -1
        node = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.size -= 1
        return node.data

    def pop_back(self):
        # 비어 있는 경우
        if self.isEmpty():
            return -1

        node = self.tail
        if self.size == 1:
            self.head = None
            self.tail = None
        elif self.size == 2:
            self.head.next = None
            self.tail = self.head
        else:
            cur = self.head
            while cur.next != node:
                cur = cur.next
            self.tail = cur
        self.size -= 1
        return node.data

    def isEmpty(self):
        return self.head is None

    def front(self):
        if self.isEmpty():
            return -1
        return self.head.data

    def back(self):
        if self.isEmpty():
            return -1
        return self.tail.data


n = int(input())
commands = [sys.stdin.readline().split() for _ in range(n)]
dq = Deque()
for command in commands:
    if 'push_front' in command:
        dq.push_front(int(command[1]))
    elif 'push_back' in command:
        dq.push_back(int(command[1]))
    elif 'pop_front' in command:
        print(dq.pop_front())
    elif 'pop_back' in command:
        print(dq.pop_back())
    elif 'size' in command:
        print(dq.size)
    elif 'empty' in command:
        if dq.isEmpty():
            print(1)
        else:
            print(0)
    elif 'front' in command:
        print(dq.front())
    elif 'back' in command:
        print(dq.back())

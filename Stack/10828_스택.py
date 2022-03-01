import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.empty():
            print(-1)
            return
        node = self.head
        self.head = self.head.next
        print(node.data)

    def size(self):
        if self.empty():
            print(0)
            return
        node = self.head
        count = 1
        while node.next is not None:
            node = node.next
            count += 1
        print(count)

    def empty(self):
        return self.head is None

    def top(self):
        if self.empty():
            print(-1)
            return
        print(self.head.data)


T = int(input())
stack = Stack()
for _ in range(T):
    command = sys.stdin.readline()
    if 'push' in command:
        stack.push(int(command.split()[-1]))
    elif 'pop' in command:
        stack.pop()
    elif 'size' in command:
        stack.size()
    elif 'empty' in command:
        if stack.empty():
            print(1)
        else:
            print(0)
    elif 'top' in command:
        stack.top()

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if self.empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def pop(self):
        if self.empty():
            return -1
        node = self.head
        self.head = self.head.next
        return node.data

    def size(self):
        count = 0
        if self.empty():
            return count
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def empty(self):
        return self.head is None

    def front(self):
        if self.empty():
            return -1
        return self.head.data

    def back(self):
        if self.empty():
            return -1
        return self.tail.data


n = int(input())
queue = Queue()
for _ in range(n):
    command = sys.stdin.readline().rstrip()
    if 'push' in command:
        queue.push(int(command.split()[-1]))
    elif 'pop' == command:
        print(queue.pop())
    elif 'size' == command:
        print(queue.size())
    elif 'empty' == command:
        if queue.empty():
            print(1)
        else:
            print(0)
    elif 'front' == command:
        print(queue.front())
    elif 'back' == command:
        print(queue.back())

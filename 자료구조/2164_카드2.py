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
        self.head = self.head.next
        return node


n = int(input())
nodes = [Node(i) for i in range(1, n + 1)]
cards = Queue()
for node in nodes:
    cards.push_back(node)

while cards.size > 1:
    cards.pop_top()
    card = cards.pop_top()
    cards.push_back(card)

print(cards.head.data)

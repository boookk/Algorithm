import sys


class MinHeap:
    def __init__(self):
        self.item = [None]

    def insert(self, data):
        self.item.append(data)
        cur_index = len(self.item) - 1
        while cur_index > 1:
            parent_index = cur_index // 2
            if self.item[parent_index] > self.item[cur_index]:
                self.item[cur_index], self.item[parent_index] = self.item[parent_index], self.item[cur_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        if len(self.item) <= 1:
            return 0

        self.item[1], self.item[-1] = self.item[-1], self.item[1]
        node = self.item.pop()
        cur_index = 1

        while cur_index <= len(self.item) - 1:
            left_child_index = cur_index * 2
            right_child_index = left_child_index + 1
            min_index = cur_index

            if left_child_index < len(self.item) and self.item[min_index] > self.item[left_child_index]:
                min_index = left_child_index
            if right_child_index < len(self.item) and self.item[min_index] > self.item[right_child_index]:
                min_index = right_child_index

            if cur_index == min_index:
                break

            self.item[cur_index], self.item[min_index] = self.item[min_index], self.item[cur_index]
            cur_index = min_index
        return node


n = int(input())
commands = [int(sys.stdin.readline()) for _ in range(n)]
heap = MinHeap()
for command in commands:
    if command != 0:
        heap.insert(command)
        continue
    print(heap.delete())

import sys


class MaxHeap:
    def __init__(self):
        self.item = [None]

    def insert(self, x):
        self.item.append(x)
        cur_index = len(self.item) - 1

        while cur_index > 1:
            parent_index = cur_index // 2
            if self.item[cur_index] > self.item[parent_index]:
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
            right_child_index = cur_index * 2 + 1
            max_index = cur_index

            if left_child_index < len(self.item) and self.item[left_child_index] > self.item[max_index]:
                max_index = left_child_index
            if right_child_index < len(self.item) and self.item[right_child_index] > self.item[max_index]:
                max_index = right_child_index

            if max_index != cur_index:
                self.item[cur_index], self.item[max_index] = self.item[max_index], self.item[cur_index]
                cur_index = max_index
            else:
                break

        return node


n = int(input())
heap = MaxHeap()
for _ in range(n):
    data = int(sys.stdin.readline())
    if data == 0:
        print(heap.delete())
    else:
        heap.insert(data)

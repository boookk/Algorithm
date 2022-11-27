import sys
import heapq
input = sys.stdin.readline


def Init(index, left, right):
    if left == right:
        seg_tree[index] = [arr[left], left]
    else:
        mid = (left + right) // 2
        Init(index * 2, left, mid)
        Init(index * 2 + 1, mid + 1, right)

        min_idx = index * 2
        if seg_tree[min_idx][value] > seg_tree[min_idx + 1][value]:
            min_idx += 1
        
        seg_tree[index] = [seg_tree[min_idx][value], seg_tree[min_idx][idx]]


def Update(index,left, right, start, end, val):
    if right < start or end < left:
        return
    if left == right:
        seg_tree[index] = [val, left]
        return
    
    mid = (left + right) // 2
    Update(index * 2, left, mid, start, end, val)
    Update(index * 2 + 1, mid + 1, right, start, end, val)
    
    min_idx = index * 2
    if seg_tree[min_idx][value] > seg_tree[min_idx + 1][value]:
        min_idx += 1
    
    seg_tree[index] = [seg_tree[min_idx][value], seg_tree[min_idx][idx]]


n = int(input())
arr = [0] + list(map(int, input().split()))
m = int(input())

value = 0
idx = 1
seg_tree = [[0, 0]] * (4 * n)
Init(1, 1, n)

for _ in range(m):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        Update(1, 1, n, cmd[1], cmd[1], cmd[2])
    else:
        print(seg_tree[1][idx])

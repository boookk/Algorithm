"""
Trie라는 자료구조를 처음 알게 되었다.
트라이는 입력되는 문자열을 Tree 형식으로 만들어 보다 빠르게 문자열 검색이 가능한 자료구조다.
보통 문자열이 존재하는지 확인 하기 위해서는 O(n)이라는 시간이 걸리지만, 
트라이 알고리즘은 O(m)으로 문자열 길이 m만큼이라는 시간이 소요된다.
빠른 시간 복잡도 덕분에 자동 완성 및 검색어 추천 기능에서 사용된다고 한다.
"""
import sys
input = sys.stdin.readline


class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, s):
        cur_node = self.root
        for c in s:
            if c not in cur_node:
                cur_node[c] = {}
            cur_node = cur_node[c]
        cur_node['*'] = {}
    
    def print_trie(self, len, cur_node=None):
        if not len:
            cur_node = self.root
        
        for c in sorted(cur_node.keys()):
            if c != '*':
                print('--' * len, c, sep='')
            self.print_trie(len + 1, cur_node[c])


n = int(input())

trie = Trie()

for _ in range(n):
    trie.insert(input().rstrip().split()[1:])

trie.print_trie(0)

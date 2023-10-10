# Trie

from sys import stdin as ss


class Trie:
    trie = dict()  # '노드': '자식'

    def add(self, l: list):
        ptr = self.trie

        for string in l:
            if string not in ptr:
                ptr[string] = {}  # string 없다면 새 자식 노드 'string': {} 생성
            ptr = ptr[string]  # 자식 노드로 포인터 이동
        #ptr['*'] = True

    def get_tree(self):
        return self.trie


n = int(ss.readline())
arr = list()

for _ in range(n):
    arr.append(list(ss.readline().split())[1:])
    
arr.sort()

trie = Trie()
for i in arr:
    trie.add(i)

d = trie.get_tree()

def print_dict(d: dict, indent=0):
    for key, value in d.items():
        print('-' * indent + key)
        if value:
            print_dict(value, indent + 2)

print_dict(d, 0)

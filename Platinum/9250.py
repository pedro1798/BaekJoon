from sys import stdin as ss
from collections import deque

class Node:
    def __init__(self):
        self.fail = None  # failure link
        self.children = dict()
        self.output = list()  #트라이의 현재 노드까지의 문자열에 포함된 keyword의 목록
    
class Problem:
    def __init__(self):  # Trie 자료구조를 매개변수로 받음
        self.trie = Node()
        
    def add(self, text: str):
        ptr = self.trie  # 루트부터 시작
        for char in text:
            if char not in ptr.children:
                ptr.children[char] = Node()
            ptr = ptr.children[char]
        ptr.output.append(text)
    
    def build_failure_links(self):
        q = deque()  # BFS 위한 queue
        
        for child in self.trie.children.values():  # 우선 root 노드의 자식 노드들의 fail -> self.trie
            child.fail = self.trie
            q.append(child)
        
        while q:  # BFS
            current_node = q.popleft()
            for char, child in current_node.children.items():
                q.append(child)
                fail_node = current_node.fail  # temp로 활용할 fail_node
                while fail_node and char not in fail_node.children:  # fail_node != self.trie and ...
                    fail_node = fail_node.fail  # fail_node pointer를 이동한다
                child.fail = fail_node.children[char] if fail_node else self.trie  # 자식 노드의 fail assign
                child.output += child.fail.output # 중요!

    def aho_corasick(self, string: str) -> str:  # Aho_Corasick O(kn + (m1, m2, ... mk))
        keyword_positions = dict()
        ptr = self.trie
        
        for char in string:
            while ptr.fail and (char not in ptr.children):
                ptr = ptr.fail  # build해둔 fail 노드로 타고 올라간다
            ptr = ptr.children[char] if (char in ptr.children) else self.trie
            
            if ptr.output:
                return True
        return False
ㅁ
    def main(self):
        for _ in range(int(ss.readline())):
            self.add((ss.readline().rstrip()))
        texts = tuple(ss.readline().rstrip() for _ in range(int(ss.readline())))
        self.build_failure_links()
        for query in texts:
            print("YES" if self.aho_corasick(query) else "NO")

            

a = Problem()
a.main()

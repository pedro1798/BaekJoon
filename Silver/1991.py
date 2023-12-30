import sys
input = sys.stdin.readline

def preorder(root):
    result = []
    if root:
        result.append(root.data)
        result.extend(preorder(root.left))
        result.extend(preorder(root.right))
    return result

def inorder(root):
    result = []
    if root:
        result.extend(inorder(root.left))
        result.append(root.data)
        result.extend(inorder(root.right))
    return result

def postorder(root):
    result = []
    if root:
        result.extend(postorder(root.left))
        result.extend(postorder(root.right))
        result.append(root.data)
    return result

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.tree = {}
        
    def add_node(self, parent, left, right):
        if parent not in self.tree:
            self.tree[parent] = Node(parent)
        if left != ".":
            self.tree[left] = Node(left)
            self.tree[parent].left = self.tree[left]
        if right != ".":
            self.tree[right] = Node(right)
            self.tree[parent].right = self.tree[right]
        
    def get_tree(self):
        return self.tree
        
if __name__ == "__main__":
    tree = BinaryTree()
    n = int(input())
    
    for _ in range(n):
        p, left, right = input().rstrip().split()
        tree.add_node(p, left, right)
    
    tree = tree.get_tree()
    
    print("".join(preorder(tree["A"])))
    print("".join(inorder(tree["A"])))
    print("".join(postorder(tree["A"])))
        

class Node:
    def __init__(self, key = None):
        self.key = key
        self.children = {}

class Trie:
    def __init__(self, node):
        self.head = node
    
    def insert(self, string):
        sarr = string.split()
        currNode = self.head

        for word in sarr:
            if word not in currNode.children:
                currNode.children[word] = Node(word)
            currNode = currNode.children[word]
    
    def search(self, node, depth):
        currNode = node
        if currNode.key != None:
            print('--' * depth + currNode.key)
            depth += 1

        keys = list(currNode.children.keys())
        if len(keys) == 0:
            return
    
        keys.sort()
        for key in keys:
            self.search(currNode.children[key], depth)

import sys
n = int(sys.stdin.readline())
k = []

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    k.append(s[2:])

node = Node()
trie = Trie(node)

for i in k:
    trie.insert(i)
trie.search(trie.head, 0)
        
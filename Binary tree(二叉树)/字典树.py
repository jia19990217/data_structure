#encoding:utf-8
#Time:2020/10/22 14:55
#Email:1215399218@qq.com
#Author:Mr.jia
#File:字典树.PY
#Software:PyCharm
class TrieNode:
    def __init__(self):
        self.data={}
        self.is_word=False
    def __repr__(self):
        return str(self.data)

class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self, word ):
        node=self.root
        for char in word:
            child=node.data.get(char)
            if child is None:
                node.data[char]=TrieNode()
            node=node.data[char]
        node.is_word=True
    def search(self,word):
        node=self.root
        for char in word:
            node=node.data.get(char)
            if not node:
                return  False
        return  node.is_word
    def startsWith(self,prefix):
        node=self.root
        for char in prefix:
            node=node.data.get(char)
            if not node:
                   return False
        return  True





a=Trie()
a.insert('sood')
a.insert('sooc')
a.insert('soor')
print(a.root.data)
print(a.search('soo'))

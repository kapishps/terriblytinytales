import urllib2
import re
import Queue as Q

class TrieNode:
    def __init__(self):
        self.nodes = dict()
        self.val = int()

    def insert_many(self, words):
        for word in words:
            self.insert(word)

    def insert(self, word):
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.val += 1


class HeapNode:
    def __init__(self , word, val):
        self.word = word
        self.val = val

    def __cmp__(self, other):
        return cmp(self.val, other.val)


pq = Q.PriorityQueue()

def solve(node, word, n):
    if node.val > 0:
        if pq.qsize() < n:
            pq.put(HeapNode(word, node.val))
        else:
            curr = pq.get()
            if curr.val < node.val:
                pq.put(HeapNode(word, node.val))
            else:
                pq.put(curr)
        # print word, node.val

    for key, value in node.nodes.items():
        solve(value, word + key, n)


def find_n_most_frequent_words(n):
    data = urllib2.urlopen('http://terriblytinytales.com/test.txt').read()
    words = re.compile('[A-Za-z]+').findall(data.lower())
    root = TrieNode()
    root.insert_many(words)
    solve(root, '', n)
    li = []
    while not pq.empty():
        temp = pq.get()
        li.append({"word" : temp.word, "freq" : temp.val})
    li.reverse()
    return li


if __name__=='__main__':
    find_n_most_frequent_words(10)
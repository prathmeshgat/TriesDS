__author__ = 'Prathmesh'
from Classes import Node as N
class Trie:

   def __init__(self):
        self.root = N.Node()

   def insert(self, word):
        self.root.insert(word)

   def get_all(self):
        return self.root.get_all()

   def get_all_with_prefix(self, prefix, string_pos = 0):
        return self.root.get_all_with_prefix(prefix, string_pos)

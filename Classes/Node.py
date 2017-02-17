__author__ = 'Prathmesh'

class Node:

    def __init__(self):
        self.word = None
        # dict of nodes
        self.nodes = dict()

    def get_all(self):
        #Get all of the words in the trie
        x = []

        #loop through each and every node in tree
        for key, node in self.nodes.items() :
            if(node.word is not None):
                x.append(node.word)

            x += node.get_all()

        return x

    def __str__(self):
        return self.word

    def insert(self, word, string_pos = 0):
        #Add a word to the node in a Trie
        current_letter = word[string_pos]

        # Create the Node if it does not already exist
        if current_letter not in self.nodes:
            self.nodes[current_letter] = Node();

        #if last character in patternString store word its leaf node
        if(string_pos + 1 == len(word)):
            self.nodes[current_letter].word = word
        else:
        	self.nodes[current_letter].insert(word, string_pos + 1)

        return True


    def get_all_with_prefix(self, prefix, string_pos):
        x = []

        for key, node in self.nodes.items() :
            # get all words which partially or fully matches prefix string
            if(string_pos >= len(prefix) or key == prefix[string_pos]):
                if(node.word is not None):
                    x.append(node.word)

                if(node.nodes != {}):
                    if(string_pos + 1 <= len(prefix)):
                        x += node.get_all_with_prefix(prefix, string_pos + 1)
                    else:
                        x += node.get_all_with_prefix(prefix, string_pos)

        return x




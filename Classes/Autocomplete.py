__author__ = 'Prathmesh'

from Classes import Trie as Tr

class Autocomplete:
    def __init__(self,word_list):

        # Create the trie and insert some words then do some tests
        self.trie = Tr.Trie()
        count = 0

        #make sure word list is present
        if(word_list is not None):
            for item in word_list:
                #make sure item is not null
                if(item is not None):
                    #make sure item is not empty string
                    if(len(item)>0):
                        count += 1;
                        self.trie.insert(item)

        # print("Count::"+str(count))


    def find(self,pattern):
        if(pattern is None):
            return None
        elif(len(pattern)<=0):
            return None
        else:
            #convert pattern to lower since all of our words are in lower case
            pattern = pattern.lower()

            returnList = list()
            returnList = self.trie.get_all_with_prefix(pattern)

            if(returnList is not None):
                if(len(returnList)>0):
                    #cleanup list to remove words with partial pattern match
                    finalList = [s for s in returnList if len(s) >= len(pattern)]
                    if(finalList is not None ):
                        if(len(finalList)>0):
                            return finalList

        #return None if no match found
        return None

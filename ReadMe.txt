Tools required:-
    Python 3.4.3
    Pycharm

Appraoach:-

    Following are main design constraints for this problem:-
    a)word_list can be extremely long, design accordingly.
    b)The find function must not loop through the whole list to find the matching words.
    c)You cannot use any third party library.

    Data structure used:-
    Considering this constraints the best  way to solve this problem is Tries,it is the
    best data structure for this problem.A trie is an n-ary tree in which characters are stored at each node.
    Each path down the tree may represent a word.

    Basically I stored all words in the form of Tries(Prefix tree). The most important
    thing to note here is in my data structure every leaf node is stores word also.

    When retrieving words matching pattern string, I just scanned the tree to find the prefix
    pattern.Once prefix pattern was found in tree I just got the words from the leaf nodes
    which are beneath the prefix branch.

    Advantages of using Tries:-
    a) There is no need to loop through whole list to find the matching words.
    b) Finding a valid prefix is very quick it takes around O(K) time where K is the length
       of pattern string.
    c) Finding the words with valid prefix is quick, we dont need to loop through all words.

Directory structure:-
    a) Classes: This folder contains all classes needed to solve this problem. It contains following files:-
        1) AutoComplete.py:- This file contains the implementation of the AutoComplete class. Note the code is
           implemented in such a way that pattern string case dosen't matter in find function.
        2) Trie.py:- This class contains the Trie class implementation. with four basic method:-
            i) constructor to set root of tree
            ii) insert method to inset word in tree.
            ii) get_all:- to get all words stored in tree
            ii) get_all_with_prefix methods gets all words which starts with pattern-string
        3) Node.py:- This class defined each node of Trie tree and it contains implementation of all methods in Trie.py.
           These implementation assumes that a given node is root node and implements all methods.

    b) Resources: This folder contains the text file with 1.1 million english words.
       I have used this as input while testing.

    c) Source:- This folder contains two files:-
       a) main.py:- This file contains code to create Autocomplete class object by passing
       word_list in constructor.IT also contains code to call find function of auto complete class,
       to find strings matching pattern.Finally it displays the results.

       b) TestSuite.py:- This file contains all test cases I used to test the autocomplete class.
       the data which I used for test is in Resources folder which consists of 1.1 millions of english words.

Instructions to runcode:-
    Use pycharm, it would be easy since project is very well organized
    a) Open project in pycharm,make sure to set interpreter as python 3.4.3
    b) Set word_list to appropriate list of words in lower case in main.py
    c) Set appropriate pattern string in find function of autoCompleteObj.
    d) Run the main.py file using the pycharm run button. If the input list contains words starting
       with prefix string then those words are displayed else the program displays message "Pattern didnt match!!!"

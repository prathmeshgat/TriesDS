__author__ = 'Prathmesh'

from Classes import Autocomplete as AC

word_list = ['aaa', 'aappp', 'aaaa']

# Construcutor takes list of words in lower case as input
autoCompleteObj = AC.Autocomplete(word_list)

#find function returns ths list of exact prefix matched words ,none if no pattern match
outputList = autoCompleteObj.find('aaa')

if(outputList is not None):
    for item in outputList:
        print(item)
else:
    print("Pattern didnt match!!!")


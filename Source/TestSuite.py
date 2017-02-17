__author__ = 'Prathmesh'

#this test suite checks the boundry conditions
#dataset used is 1.1 million english words

import os
from os import path
from Classes import Autocomplete as AC


word_list=[]
FILE_PATH = path.join(os.pardir, "Resources/1.1million_word_list.txt")
f = open(FILE_PATH)

for line in f:
    tempList = line.split("\n");
    word_list.append(tempList[0].lower())

f.close()


#test case 1
#input:: word_list= 1.1 million words,pattern_string = "prath"
#expected output:: ['prathuang', 'prathe', 'pratheep', 'prather', 'pratham', 'prathapan']
autoCompleteObj = AC.Autocomplete(word_list)
outputList = autoCompleteObj.find("prath")
expList = ['prathuang', 'prathe', 'pratheep', 'prather', 'pratham', 'prathapan']

if(outputList is None):
    print("Failed test case 1")
elif(set(outputList) == set(expList)):
    print("passed test case 1")
else:
    print("Failed test case 1")

#test case 2
#input:: word_list= list on 1.1 million words, pattern_string = None
#expected output:: NONE
outputList = autoCompleteObj.find(None)
if(outputList is None):
    print("Passed test case 2")
else:
    print("Failed test case 2")

#test case 3
#input:: word_list= list on 1.1 million words,pattern_string = "kshitj" [this is unmatched pattern]
#expected output:: NONE
outputList = autoCompleteObj.find("kshitj")

if(outputList is None):
    print("Passed test case 3")
else:
    print("Failed test case 3")


#test case 4
#input:: word_list= empty list,pattern_string = "kshitj" [this is unmatched pattern]
#expected output:: NONE
autoCompleteObj = AC.Autocomplete([])
outputList = autoCompleteObj.find("kshitj")

if(outputList is None):
    print("Passed test case 4")
else:
    print("Failed test case 4")

#test case 5
#input:: word_list= None,pattern_string = "kshitj" [this is unmatched pattern]
#expected output:: NONE
autoCompleteObj = AC.Autocomplete(None)
outputList = autoCompleteObj.find("kshitj")

if(outputList is None):
    print("Passed test case 5")
else:
    print("Failed test case 5")

#test case 6
#input::
# word_list = ['aardvark', 'altimeter', 'apotactic', 'bagonet', 'boatlip', 'carburant', 'chyliferous', 'consonance', 'cyclospondylic', 'dictyostele', 'echelon', 'estadal', 'flaunty', 'gesneriaceous',
#'hygienic', 'infracentral', 'jipijapa', 'lipoceratous', 'melanthaceae']
#pattern_string = 'a'
#expected output::  ['aardvark', 'altimeter', 'apotactic']

word_list = ['aardvark', 'altimeter', 'apotactic', 'bagonet', 'boatlip', 'carburant', 'chyliferous', 'consonance', 'cyclospondylic', 'dictyostele', 'echelon', 'estadal', 'flaunty', 'gesneriaceous',
'hygienic', 'infracentral', 'jipijapa', 'lipoceratous', 'melanthaceae']
autoCompleteObj = AC.Autocomplete(word_list)
outputList = autoCompleteObj.find('a')

expList = ['aardvark', 'altimeter', 'apotactic']

if(outputList is None):
    print("Failed test case 6")
elif(set(outputList) == set(expList)):
    print("passed test case 6")
else:
    print("Failed test case 6")


#test case 7
#input::
# word_list = ['angiohydrotomy', 'angiospermal', 'anglist', 'angularization', 'anhungry', 'animalcule', 'anisaldehyde', 'anisometric', 'ankylenteron', 'annette']
#pattern_string = 'ani'
#expected output::   ['animalcule', 'anisaldehyde', 'anisometric']

word_list = ['angiohydrotomy', 'angiospermal', 'anglist', 'angularization', 'anhungry', 'animalcule', 'anisaldehyde', 'anisometric', 'ankylenteron', 'annette']
autoCompleteObj = AC.Autocomplete(word_list)
outputList = autoCompleteObj.find('ani')

expList =  ['animalcule', 'anisaldehyde', 'anisometric']

if(outputList is None):
    print("Failed test case 7")
elif(set(outputList) == set(expList)):
    print("passed test case 7")
else:
    print("Failed test case 7")


#test case 8
#input::
# word_list = ['bagonet', 'consonance', 'estadal', 'hygienic', 'melanthaceae', 'overwander', 'prototypographer', 'siphonocladales', 'transferography', 'venturesomeness']
#pattern_string = 'venture'
#expected output::    ['venturesomeness']

word_list = ['bagonet', 'consonance', 'estadal', 'hygienic', 'melanthaceae', 'overwander', 'prototypographer', 'siphonocladales', 'transferography', 'venturesomeness']
autoCompleteObj = AC.Autocomplete(word_list)
outputList = autoCompleteObj.find('venture')

expList =  ['venturesomeness']

if(outputList is None):
    print("Failed test case 8")
elif(set(outputList) == set(expList)):
    print("passed test case 8")
else:
    print("Failed test case 8")

#test case 9
#input::word_list = ['anisaldehyde', 'anisometric', 'ankylenteron']
# word_list = ['bagonet', 'consonance', 'estadal', 'hygienic', 'melanthaceae', 'overwander', 'prototypographer', 'siphonocladales', 'transferography', 'venturesomeness']
#pattern_string = 'foobar'
#expected output::    None

word_list = ['anisaldehyde', 'anisometric', 'ankylenteron']
autoCompleteObj = AC.Autocomplete(word_list)
outputList = autoCompleteObj.find('foobar')

if(outputList is None):
    print("passed test case 9")
else:
    print("Failed test case 9")


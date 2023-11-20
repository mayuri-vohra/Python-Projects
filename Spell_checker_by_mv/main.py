from textblob import TextBlob
from spellchecker import SpellChecker

f=open('demo.txt','r')
data=str(f.read())
print(data)
# you can also use list of misspelled words
print("\n\n**************************Using textblob**************************************")
misspelled_word_list= data.split()
for word in misspelled_word_list:
    correct_word=TextBlob(word).correct()
    print("\nWord: ",word)
    print('------------------------------')
    print("Corrected Word: ",correct_word)
    print("\n================================")

print('\n***************************Using pyspellchecker***********************************')
spell=SpellChecker()
misspelled_word=spell.unknown(misspelled_word_list)
print(type(misspelled_word))
for word in misspelled_word:
    print("\nword: ",word)
    print('--------------------------------------------')
    print("Corrected word is ", spell.correction(word))
    print('--------------------------------------------')
    print("Candidate words:",spell.candidates(word))
    print("\n================================")

f.close()
from nltk.corpus import wordnet as wordnet
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from collections import Counter
import nltk
import pdb

sentence = input().lower()
words = nltk.pos_tag(word_tokenize(sentence))
print(words)

count= Counter([j for i,j in pos_tag(word_tokenize(sentence))])
print (count)

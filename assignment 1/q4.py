import re
from operator import itemgetter
import nltk

import math

frequency = {}
tokens = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))

words = []
for word in tokens:
    x= word.lower()
    words.append(x)

stop_words = nltk.corpus.stopwords.words('English')
words_ns=[]
for word in words:
    if word not in stop_words:
        words_ns.append(word)

uw = len(set(words_ns))
print("Total number of tokens in the corpus: ",len(tokens))
m=21*pow(len(tokens),0.48)
print("Unique number of words according to heaps law:",m)
print("Number of unique words: ", uw)

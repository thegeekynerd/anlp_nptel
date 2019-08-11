import requests
import re
from bs4 import BeautifulSoup as BS
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

url = 'http://shakespeare.mit.edu/allswell/full.html'
r = requests.get(url)
html = r.text

#soup = BS(html,'html5lib')
#text = soup.get_text()
#soup_new = soup.findAll('blockquote')

file = open("allswell.txt",'r')
text = file.read()
file.close()

tokenizer = RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(text)
tokens_sent = sent_tokenize(text)
#tokens = word_tokenize(text)

BERTRAM = 0
Bertram = 0
for token in tokens:
    if token == "BERTRAM":
        BERTRAM=BERTRAM+1
    elif token == "Bertram":
        Bertram=Bertram+1

print("Bertram: ",Bertram)
print("BERTRAM: ",BERTRAM)

sent_n=len(tokens_sent)
word_n=len(tokens)

print("Number of words: ",word_n)
print("Number of sentences: ",sent_n)
print("Average sentence length of this document is: ",(word_n/sent_n))

words = []
for word in tokens:
    x= word.lower()
    if x not in words:
        words.append(x)

stop_words = nltk.corpus.stopwords.words('English')
words_ns=[]
for word in words:
    if word not in stop_words:
        words_ns.append(word)

uw = len(set(words_ns))
print("Number of unique words: ", uw)

tokens_w = word_tokenize(text)
count = 0
for token in tokens_w:
    if token=='!':
        count+=1
print("Count of words preceding exclamatory: ", count)

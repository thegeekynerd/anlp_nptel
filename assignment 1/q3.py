import re
from operator import itemgetter
import nltk
import pandas as pd
import math

frequency = {}
words_emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))

for word in words_emma:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

#Zipf's law
rank = 1;
column_header = ['Rank', 'Frequency', 'Frequency*Rank']
tf_row = []
row = []
df = pd.DataFrame(columns=column_header)
pd_cols = []
rows = []

for word, freq in reversed(sorted(frequency.items(), key=itemgetter(1))):
    df.loc[word] = [rank,freq,rank*freq]
    rank = rank+1
    

print(df)


#Mandelbrot's Approximation

rank = 1;
column_header = ['Rank', 'Frequency', 'Frequency*Rank+\u03B2']
tf_row = []
row = []
df = pd.DataFrame(columns=column_header)
pd_cols = []
rows = []

for word, freq in reversed(sorted(frequency.items(), key=itemgetter(1))):
    df.loc[word] = [rank,freq,(rank+2.7)*freq]
    rank = rank+1
    

print(df)

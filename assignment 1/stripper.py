import requests
import re
from bs4 import BeautifulSoup as BS
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize


#cleaning and extracting
url = 'http://shakespeare.mit.edu/allswell/full.html'
r = requests.get(url)
html = r.text

soup = BS(html,'html5lib')
text = soup.get_text()
blockquote = soup.findAll('blockquote')

tokenizer = RegexpTokenizer('\w+[\']*\w*')
tokens = tokenizer.tokenize(text)

s=''
for block in blockquote:
    try:
        lines = block.find_all('a')
        for line in lines:
            s+=line.text+' '
            
    except:
        continue


new = " ".join(s.split())

file = open("allswell.txt",'w')
file.write(new)
file.close()

#code for nlp starts


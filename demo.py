# -*-coding=utf-8-*-
from nltk.stem.wordnet import WordNetLemmatizer
import re

def my_stemming(content):
    word_list = re.compile('\s+').split(content)
    print(word_list)
    cont_list = []
    for w in word_list:
        if w not in stopwds:
            cont_list.append(w)
    wnl = WordNetLemmatizer()
    s = wnl.lemmatize('a request')
    print(s)
    pass

# my_stemming('a requests')


a = '1'
b = '2'
c = '3'
d = '4'
result = ' '.join([a,b,c,d])
print(result)
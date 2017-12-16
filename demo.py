# -*-coding=utf-8-*-
from nltk.stem.wordnet import WordNetLemmatizer
import re

# sentence = 'A server MUST respond with a 400 status code to any HTTP/1.1 ' \
#            'request message that lacks a Host header feld and to any request ' \
#            'message that contains more than one Host header feld or a Host ' \
#            'header feld with an invalid feld-value. '


sentence = 'A server MUST respond with a 400 (Bad Request) status code to any HTTP/1.1 request message that lacks a Host header feld and to any request message that contains more than one Host header feld or a Host header feld with an invalid feld-value. '

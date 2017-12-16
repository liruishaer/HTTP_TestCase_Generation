# -*- coding=utf-8 -*-
import en_core_web_sm
from spacy import displacy    # 查看地址：http://127.0.0.1:5000/
nlp = en_core_web_sm.load()


sentence = 'A server MUST respond with a 400 status code to any HTTP/1.1 request message that lacks a Host header feld and to any request message that contains more than one Host header feld or a Host header feld with an invalid feld-value. '

# 目标句子（分解之后的句子）
# sentence = 'A server MUST respond with a 400 status code to any HTTP/1.1 request message that lacks a Host header feld;' \
#            'A server MUST respond with a 400 status code to any request message that contains more than one Host header feld' \
#            'A server MUST respond with a 400 status code to any request message that  a Host header feld with an invalid feld-value. '

doc = nlp(sentence)

# replace entities and noun chuncks
spans = list(doc.ents) + list(doc.noun_chunks)
for span in spans:
    span.merge()

displacy.serve(doc, style='dep')   # 实体：ent   依存：dep

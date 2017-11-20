# -*- coding=utf-8 -*-

# 法一：加载英文模型
# import spacy
# # print(spacy.info())  # 获得spacy相关信息
# # nlp = spacy.load('en')  # load model with shortcut link "en"
# nlp = spacy.load('en_core_web_sm')   # load model package "en_core_web_sm"

# 法二：加载英文模型（推荐）
import en_core_web_sm
nlp = en_core_web_sm.load()


sentence = 'A sender  MUST NOT send a request with multiple headers with the same name.'
# sentence = 'I would like to eat apple.'


doc = nlp(sentence)
print(doc.is_parsed)  # 监测一个文档是否进行了依存分析
# print([(w.text, w.pos_)for w in doc])


# 1. POS Tagging
print('POS Tagging.....')
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)
'''
token.text:  原文本
token.lemma_:  词干化
token.pos_:
token.tag_:
token.dep_:
token.shape_: 大小写等形状（我不会用）
token.is_alpha: 是否为字母单词（neo4j->False）
token.is_stop: 是否为停用词
'''


# 2. Noun chunks
print('\n\nNoun chuncks......')
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_,
          chunk.root.head.text)


# 3. Navigating the parse tree(句法依存树)
print('\n\nNavigating the parse tree......')
doc = nlp(u'Autonomous cars shift insurance liability toward manufacturers')
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
          [child for child in token.children])

# # 3. visualizing the dependency   查看地址：http://127.0.0.1:5000/
# from spacy import displacy
# sentence = 'A sender must not send a request with multiple headers with the same name.'
# doc = nlp(sentence)
# # options = {'ents': ['ORG']}  # 只选择表特定类型的实体
# # displacy.serve(doc, style='ent', options=options)
# displacy.serve(doc,style='dep')
# # displacy.serve(doc, style='dep')   # 实体：ent   依存：dep


# 4. named entity
print('\n\nnamed entity......')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
import en_core_web_sm
nlp = en_core_web_sm.load()

# 3. visualizing the dependency   查看地址：http://127.0.0.1:5000/
from spacy import displacy
sentence = 'A sender must not send a request with multiple headers with the same name.'
# sentence = 'A flower.'
doc = nlp(sentence)
displacy.serve(doc, style='dep')   # 实体：ent   依存：dep

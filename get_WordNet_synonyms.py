from nltk.corpus import wordnet

# syns = wordnet.synsets('program')
# # An example of a synset:
# print(syns[0].name())
# # Just the word:
# print(syns[0].lemmas()[0].name())
# # Definition of that first synset:
# print(syns[0].definition())
# # Examples of the word in use in sentences:
# print(syns[0].examples())


synonyms = []
antonyms = []
for syn in wordnet.synsets("one"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print('synonyms:',set(synonyms))
print('antonyms:',set(antonyms))




# w1 = wordnet.synset('run.v.01') # v here denotes the tag verb
# w2 = wordnet.synset('jump.v.01')
# print(w1.wup_similarity(w2))




# w1 = wordnet.synset('ship.n.01')
# w2 = wordnet.synset('boat.n.01') # n denotes noun
# print(w1.wup_similarity(w2))

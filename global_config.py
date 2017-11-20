# -*- coding=utf-8 -*-
import nltk
import re
import esm


# 文件名
rfc7230_file = './corpus/RFC7230.txt'
rfc2616_file = './corpus/RFC2616.txt'
tmp_file = './corpus/tmp.txt'
contain_modal_file_7230 = './corpus/7230_contain_modal_sentences.txt'
contain_modal_file_2616 = './corpus/2616_contain_modal_sentences.txt'


# 变量
SUBJECTS = ["nsubj", "nsubjpass", "csubj", "csubjpass"]#, "agent", "expl"]
OBJECTS = ["dobj", "dative", "oprd"]   #"attr",
AUXVERT = ['aux', 'auxpass']
Modal_Words = ['could','should','must','shall','can','would','may','might','need', 'have','ought','either','has']
modal_patern = '(.*( could| should| mush| shall| can| would| may| might| have .* to | had .* to |' \
               ' having .* to | has .* to | either .* or | neither .* nor | ought .* to | need .* to ).*)'

modal_pattern_list = ['.* could .*','.* should .*','.* mush .*','.* shall .*',
                      '.* can .*','.* would .*','.* may .*','.* might .*',
                      '.* have .* to .*','.* had .* to .*','.* having .* to .*',
                      '.* has .* to .*','.* either .* or .*','.* neither .* nor .*',
                      '.* ought .* to .*','.* need .* to .*']

'''根据字典构造AC树'''
def makeACTree(wordList = []):
    esmreIndex = esm.Index()
    for word in wordList:
        esmreIndex.enter(word)
    esmreIndex.fix()

    return esmreIndex

MODAL_ACTree = makeACTree(Modal_Words)






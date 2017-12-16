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
SUBJECTS = ["nsubj", "nsubjpass", "csubj", "csubjpass", "expl"]
OBJECTS = ["dobj", "dative", "oprd",'pobj','iobj','obj','oprd',"agent"]   #"attr",
AUXVERT = ['aux', 'auxpass']
ATTRS = ['prep','appos','attr']
DETERMINER_POS = ['DT','IN']   # 限定词的词性
DETERMINER_DEP = ['det']   # 限定词的依存关系
MODAL_POS = ['MD']

MODAL_CAPITAL_WORDS = ["MUST", "SHOULD", "RECOMMENDED", "MUST NOT", "SHOULD NOT", "MAY"]
Modal_Words = ['could','should','must','shall','can','would','may','might','need', 'have','ought','either','has']
modal_patern = '(.*( could| should| mush| shall| can| would| may| might| have .* to | had .* to |' \
               ' having .* to | has .* to | either .* or | neither .* nor | ought .* to | need .* to ).*)'

modal_pattern_list = ['.* could .*','.* should .*','.* must .*','.* shall .*',
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



# mapping
Request_URL_List = ['http://www.baidu.com/']
HTTP_Version = 'HTTP/1.1'

Method_Dict = {'OPTIONS': [],
            'GET': ['get','fetch','obtain'],
            'HEAD': [],
            'POST': [],
            'PUT': [],
            'DELETE': [],
            'TRACE': [],
            'CONNECT': []
            }
Request_Header = {'Host':['host'],'Accept':[],
                  'Accept-Charset':[],'Accept-Encoding':[],
                  'Accept-Language':[],'Authorization':[],
                  'Expect':[],'From':[],'If-Match':[],
                  'If-Modified-Since':[],'If-None-Match': [],
                  'If-Range':[],'If-Unmodified-Since':[],
                  'Max-Forwards':[],'Proxy-Authorization':[],
                  'Range':[],'Refere':[],'TE':[],'User-Agent':[]}

# test case



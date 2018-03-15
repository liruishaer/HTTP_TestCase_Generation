# -*- coding=utf-8 -*-
'''
function: finding sentences that describe particular rule type (for example: header_copy)
author: lirui
date: 2018-01-21
'''

words = '''1. multiple
2. more than one, more than a/an, more than, one or more, at least one,at least
3. lack, lack of, lacking
4. various, a variety of,diverse
5. many, little, no
6. multifarious,multifaceted
7. a number of
8. over
9. several
10. a large number of
11. absence
12. be short of, short of
13. disappearance
14. be pressed for
15. without
16. missing,loss,omit
17. shortage, shortage of
18. leastwise, at least, at the least
19. single,double,one'''


# all_words = []
# for line in words.split('\n'):
#     line = line.strip().split('.')[1]
#     lst = line.split(',')
#     all_words += [wd.strip() for wd in lst]
#
# print(all_words)

words = [' multiple ', ' more than ', ' one or more ', ' at least one ', ' at least ', ' lack ', ' various ', ' a variety of ', ' diverse ', ' many ', ' little ', ' no ', ' multifarious ', ' multifaceted ', ' a number of ', ' over ', ' several ', ' a large number of ', ' absence ', ' be short of ', ' short of ', ' disappearance ', ' be pressed for ', ' without ', ' missing ', ' loss ', ' omit ', ' shortage ', ' shortage of ', ' leastwise ', ' at the least ', ' single ', ' double ', ' one ']

# 通用首部字段
COMMON_headers = ['Cache-Control','Connection','Date','Pragma','Trailer',
                  'Transfer-Encoding','Upgrade','Via','Warning']
# 请求首部字段(现在要做的)
REQUEST_headers = ['Accept','Accept-Charset','Accept-Encoding','Accept-Language',
                   'Authorization','Expect','From','Host','If-Match',
                   'If-Modified-Since','If-None-Match','If-Range','If-Unmodified-Since',
                   'Max-Forwards','Proxy-Authorization','Range','Referer','TE','User-Agent']
# 响应首部字段
RESPOUND_headers = ['Accept-Ranges','Age','Content-Disposition','ETag,Location',
                    'Proxy-Authenticate','Retry-After','Server','Vary','WWW-Authenticate']

# 实体首部字段
ENTITY_headers = ['Allow','Content-Encoding','Content-Language','Content-Length','Content-Location',
                  'Content-MD5','Content-Range','Content-Type','Expires','Last-Modified']

omit_headers = COMMON_headers + RESPOUND_headers + ENTITY_headers

def type_rule_mapping():
    '''
    one 后面必须为名词, 不能为形容词/介词； 不好的词：over, without no
    :return:
    '''
    infile = './corpus/2616_contain_modal_sentences.txt'
    sentence_list = [line.strip() for line in open(infile,'r') if line.strip()!='' and not line.startswith('[.*')]

    for sent in sentence_list:
        # 1. 过滤掉暂时不处理的headers
        for header in omit_headers:
            if header in sent.replace(' ',''):
                continue

        # 2. 获取当前句子的header_name
        cur_header_name_list = []
        for header in REQUEST_headers:
            if header in sent.replace(' ',''):
                cur_header_name_list.append(header)


        flag = False
        tmp_list = []
        for wd in words:
            if wd in sent:
                flag = True
                tmp_list.append(wd)


        if flag and ' field' in sent:
            print('**','\t|\t'.join(tmp_list),'  ###  ',';'.join(cur_header_name_list))
            print(sent)
            print('\n')





type_rule_mapping()
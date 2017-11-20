# -*- coding=utf-8 -*-
from global_config import *

def get_sentences(rfc_file):
    sentences = []
    # 获取content
    pattern = '^(\s+).*'  # 行首的空白符
    content = ''
    last_space = ''
    cur_space = ''
    for line in open(rfc_file,'r'):
        match_results = re.compile(pattern).findall(line)
        if len(match_results):
            cur_space = match_results[0]
        else:
            cur_space = ''

        line = line.strip()
        if cur_space!=last_space:
            content += '\n'+line
        else:
            content += ' ' + line

        last_space = cur_space

    # 去除页眉页脚
    pattern = '\s+Fielding, et al.*\s+.*\s+'
    content = re.compile(pattern).sub(' ',content)
    content = content.replace('e.g.','e.g,')

    content_list = content.split('\n')
    for cont in content_list:
        sentences += nltk.sent_tokenize(cont)

    # for sent in sentences:
    #     print(sent)
    return sentences




def match_modal(outfile,rfc_file):
    sentences = get_sentences(rfc_file)
    fout = open(outfile, 'w')

    for sent in sentences:
        tags = ''
        flag = False
        for pattern in modal_pattern_list:
            results = re.findall(pattern, sent)
            if results:
                flag = True
                tags += '['+ pattern+']'
        if flag:
            fout.write(tags+'\n'+sent+'\n\n\n\n')
    fout.close()



# match_modal(contain_modal_file_2616,rfc2616_file)
match_modal(contain_modal_file_7230,rfc7230_file)



# 词性过滤
# -*- coding=utf-8 -*-
'''
function: 过滤带有情态动词的句子
'''
from global_config import *
import nltk

def get_sentences(rfc_file):
    sentences = []
    # 获取content
    pattern_space = '^(\s+).*'  # 行首的空白符
    pattern_unword = '(^(\s+)[^a-zA-Z]*)'  # 行首的非字母字符
    content = ''
    last_space = ''
    cur_space = ''

    last_unword_len = 0
    cur_unword_len = 0

    for line in open(rfc_file,'r'):
        line = line.strip()
        if line.strip()=='':
            content += '\n'
            continue

        space_results = re.compile(pattern_space).findall(line)
        if len(space_results):
            cur_space = space_results[0]
        else:
            cur_space = ''

        unword_results = re.compile(pattern_unword).findall(line)
        if len(unword_results) and len(unword_results[0]):
            cur_unword_len = len(unword_results[0])
        else:
            cur_unword_len = 0

        if cur_space != last_space:
            # 比较unword长度
            if cur_unword_len == last_unword_len:
                content += ' ' + line
            else:
                content += '\n'+line
        else:
            content += ' ' + line

        last_space = cur_space
        last_unword_len = cur_unword_len

    # 去除页眉页脚
    pattern = '\s+Fielding, et al.*\s+.*\s+'
    content = re.compile(pattern).sub(' ',content)
    content = content.replace('e.g.','e.g,')

    content_list = content.split('\n')
    for cont in content_list:
        sentences += nltk.sent_tokenize(cont)

    # for sent in sentences:
    #     print(sent)
    print('get_sentence() over!')
    return sentences


def match_modal(outfile,rfc_file,pattern_list):
    sentences = get_sentences(rfc_file)
    fout = open(outfile, 'w')

    pattern_list += [pattern.upper() for pattern in pattern_list]
    print(pattern_list)
    print('len pattern list', len(pattern_list))
    for sent in sentences:
        tags = ''
        flag = False
        for pattern in pattern_list:
            # pattern = pattern.upper()
            results = re.findall(pattern, sent)
            if results:
                flag = True
                tags += '['+ pattern+']\t'
        if flag:
            fout.write(tags+'\n'+sent+'\n\n\n\n')
    fout.close()



# def match_modal(outfile,rfc_file):
#     sentences = get_sentences(rfc_file)
#     fout = open(outfile, 'w')
#
#     for sent in sentences:
#         fout.write(sent + '\n\n\n\n')
#     fout.close()



# match_modal(contain_modal_file_2616,rfc2616_file,modal_pattern_list)
# match_modal(contain_modal_file_7230,rfc7230_file,modal_pattern_list)

match_modal('./corpus/7230_contain_all_modal_sentences.txt',rfc7230_file,modal_pattern_list)


# pattern_asn_list = ['::=']
# match_modal('./rfc_ssl/1_rfc5280_contain_modal_sentence.txt','./rfc_ssl/rfc5280.txt',pattern_asn_list)
# match_modal('./rfc_ssl/1_rfc6818_contain_modal_sentence.txt','./rfc_ssl/rfc6818.txt',pattern_asn_list)




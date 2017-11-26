# -*- coding=utf-8 -*-
'''
function: 对句子进行句法分析，得到主谓宾元祖
author:lirui
date:2017-11-15
'''
from global_config import *
from nltk.stem.wordnet import WordNetLemmatizer
import re
import en_core_web_sm
from subject_object_extraction import findSVOs,printDeps
nlp = en_core_web_sm.load()

sentence = 'A good sender must not send a request with multiple headers with the same name.'
# sentence = 'A sender MUST NOT generate multiple header felds with the same feld name in a message.'
# sentence = 'A server MUST respond with a 400 (Bad Request) status code to any HTTP/1.1 request message that lacks a Host header feld and to any request message that contains more than one Host header feld or a Host header feld with an invalid feld-value. '
# sentence = 'The "*" value must not be generated by a proxy server; it may only be generated by an origin server.'
# sentence = 'All responses to the HEAD request method MUST NOT include a message-body, even though the presence of entity- header fields might lead one to believe they do.'



def my_stem(token_list):
    result_token_list = []

    for token in token_list:
        print(token.text,token.tag_)
        # 过滤介词/限定词
        if token.tag_  in DETERMINER_POS or token.dep_  in DETERMINER_DEP:
            continue

        result_token_list.append(token)
    return result_token_list


def get_attr_dict(token):

    processed_list = []

    # for child in token.children:
    #     result = child_recursion(child,processed_list)
    result = child_recursion(token,processed_list)
    print('递归：')
    print(result)


def child_recursion(token,procesed_list):
    if token not in procesed_list:
        procesed_list.append(token)
    else:
        return {}

    # 过滤介词/限定词
    if token.tag_ in DETERMINER_POS or token.dep_ in DETERMINER_DEP:
        tmp_dict = {}
        for child in token.children:
            key = token.text
            value = child_recursion(child,procesed_list)
            if value:
                tmp_dict[key] = value
        return tmp_dict

    # if not token.children:   # 没有孩子
    #     key = token.text
    #     value = token.dep_
    #     return {key:value}
    # else:   # 有孩子
    flag_hasChildren = False
    tmp_dict = {}
    for child in token.children:
        flag_hasChildren = True
        key = token.text
        value = child_recursion(child, procesed_list)
        if value:
            tmp_dict[key] = value
    if flag_hasChildren == False:
        key = token.text
        value = token.dep_
        return {key:value}
    else:
        return tmp_dict






def extract_modifier(token):
    result = {}
    attr_list = []
    for child in token.children:
        if child.dep_ in ATTRS:
            # 去除无意义词汇
            # subtree_list = my_stem(child.subtree)
            tmp_rst = {}
            my_result = get_attr_dict(child)

            # for tk in subtree_list:

            subtree_str = ''.join([w.text_with_ws for w in child.subtree])
            if subtree_str:
                attr_list.append(subtree_str)
    if attr_list:
        result['attr_list'] = attr_list

    return result



def extract_info(sentence):
    print(sentence)
    doc = nlp(sentence)

    # replace entities and noun chuncks
    # spans = list(doc.ents) #+ list(doc.noun_chunks)
    # for span in spans:
    #     span.merge()

    # 先找助动词
    modals = []
    for i in range(len(doc)):
        token = doc[i]
        # if token.text.lower() in Modal_Words and token.pos_ == 'VERB' and token.pos_ in MODAL_POS:
        print(token.text,token.tag_)
        if token.tag_ in MODAL_POS:
            modals.append((i,token))

    if not modals:
        print('没有发现情态动词！！！！')
        return

    result_list = []   # [{'subject':{},'predicate':{'word':'','neg':'False/True'},'object':{}}  ...]
    for modal in modals:
        result = {}
        index = modal[0]
        token = modal[1]

        # 根据情态动词找其修饰的谓语
        if token.head.pos_ == 'VERB':
            predicate_token = token.head
            result['predicate'] = {'key':predicate_token.text,'modal':token.text}
            # 谓语的修饰语--------------------------------------------------------------------
            rst = extract_modifier(predicate_token)    # 提取修饰语
            for key in rst:
                result['predicate'][key] = rst[key]

            # 判断是否有否定词--------------------------------------------------------------------
            if index + 1 < len(doc):
                if doc[index + 1].text.lower() == 'not':
                    result['predicate']['neg'] = True
                else:
                    result['predicate']['neg'] = True
            else:
                result['predicate']['neg'] = False

            # 从谓语往下找
            for token in predicate_token.children:
                # 找主语-------------------------------------------------------------------------
                if token.dep_ in SUBJECTS:
                    result['subject'] = {'key':token.text}
                    rst = extract_modifier(token)   # 提取修饰语
                    for key in rst:
                        result['subject'][key] = rst[key]

                # 找宾语 ---------------------------------------------------------------------------
                if token.dep_ in OBJECTS:
                    result['object'] = {'key':token.text}
                    rst = extract_modifier(token)   # 提取修饰语
                    for key in rst:
                        result['object'][key] = rst[key]




        print(result)




extract_info(sentence)
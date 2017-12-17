# -*- coding=utf-8 -*-
import en_core_web_sm
from spacy import displacy    # 查看地址：http://127.0.0.1:5000/
nlp = en_core_web_sm.load()


# sentence = 'A server MUST respond with a 400 status code to any HTTP/1.1 request message that lacks a Host header feld and to any request message that contains more than one Host header feld or a Host header feld with an invalid feld-value!'
sentence = 'China and America is big country  in the world.'

# 目标句子（分解之后的句子）
# sentence = 'A server MUST respond with a 400 status code to any HTTP/1.1 request message that lacks a Host header feld;' \
#            'A server MUST respond with a 400 status code to any request message that contains more than one Host header feld' \
#            'A server MUST respond with a 400 status code to any request message that  a Host header feld with an invalid feld-value. '


'''判断是否含有并列关系'''
def has_conj_relation(token):
    flag = False
    for tk in token.subtree:
        if tk.dep_ in ['conj']:
            flag = True
    return flag



'''长句切分'''
def cut_long_sentence(sentence):
    '''
    根据并列的依存关系进行句子切分；找到句子的核心词，根据祖先和孩子找
    :param sentence:
    :return:
    '''
    print(sentence)
    print('************************************')
    doc = nlp(sentence)

    # 1. 实体和名词替换
    spans = list(doc.ents) + list(doc.noun_chunks)
    for span in spans:
        span.merge()

    # 2. 找到句子的root
    root_token = doc[:].root
    print(root_token)
    print('*'*50)
    # subtree_span = doc[root_token.left_edge.i: root_token.right_edge.i + 1]
    # print(subtree_span.text, '|', subtree_span.root.text)

    # subtree_span = doc[2:5]
    # print(subtree_span.text, '|', subtree_span.root.text)
    # print('#' * 50)



    # for tk in root_token.lefts:
    #     for w in tk.subtree:
    #         if w.dep_ in ['cc','conj']:
    #             print('有并列关系')
    #
    #     # print([child for child in (tk.ancestors)])
    #     # sublist = [w.text_with_ws for w in tk.subtree]
    #     # subtree_str = ' '.join(sublist)
    #     # subtree_str = ' '.join([w.text_with_ws for w in child.subtree])
    #     # print(subtree_str)

    conj_token = [token for token in doc if token.dep_ in ['conj']]
    # 合并相连的连接词
    for tk in conj_token[::-1]:
        tk_parent = tk.head.head
        tk_conj = tk.head
        print(tk,'|',tk_conj,'|',tk_parent)

        # 当前的substr
        print('substr: ',' '.join([w.text_with_ws for w in tk.subtree]))

        # 并列关系的substr
        conj_substr = tk_conj.text
        for tkw in tk_conj.children:
            if tkw.dep_ not in ['conj','cc']:
                conj_substr += ' '.join([w.text_with_ws for w in tkw.subtree])
        print(conj_substr,'\n')

        # parent所组成的字符串
        prtstr = ''
        ancestor_list = [tkw for tkw in tk_conj.ancestors]
        ancestor_str_list = [tkw.text for tkw in tk_conj.ancestors]
        for ancestor in ancestor_list[:]:
            for tkw in ancestor.children:
                if tkw != tk_conj:
                    ancestor_str_list.append(' '.join([w.text_with_ws for w in tkw.subtree]))
        print(ancestor_str_list)





        break











if __name__ == '__main__':
    # extract_info(sentence)
    cut_long_sentence(sentence)

# -*- coding=utf-8 -*-
import re
from collections import defaultdict
# import nltk
# import nltk.stem
# from nltk.corpus import stopwords
# import en_core_web_sm
# nlp = en_core_web_sm.load()

def get_sentences(rfc_file):
    sentences = []
    # 获取content
    pattern = '^(\s+).*'  # 行首的空白符
    content = ''
    last_space = ''
    cur_space = ''
    for line in open(rfc_file, 'r'):
        match_results = re.compile(pattern).findall(line)
        if len(match_results):
            cur_space = match_results[0]
        else:
            cur_space = ''

        line = line.strip()
        if cur_space != last_space:
            content += '\n' + line
        else:
            content += ' ' + line

        last_space = cur_space

    # 去除页眉页脚
    pattern = '\s+Fielding, et al.*\s+.*\s+'
    content = re.compile(pattern).sub(' ', content)
    content = content.replace('e.g.', 'e.g,')

    content_list = content.split('\n')
    for cont in content_list:
        sentences += nltk.sent_tokenize(cont)

    # for sent in sentences:
    #     print(sent)
    return sentences


def statistic_verbword(outfile,rfc_file1,rfc_file2):
    my_stemmer = nltk.stem.SnowballStemmer('english')

    result = {}

    sentences1 = get_sentences(rfc_file1)
    sentences2 = get_sentences(rfc_file2)
    sentences = sentences1 + sentences2
    count = 0
    for sent in sentences:
        count += 1
        print(count)
        # if i > 100:break
        tokens = nltk.word_tokenize(sent)
        pos_list = nltk.pos_tag(tokens)
        for i in range(len(pos_list)):
            pos = pos_list[i][1]
            # 找动词
            if pos in ['VBP', 'VB', 'VBD', 'VBG', 'VBN', 'VBZ']:
                # 去停用词
                word = my_stemmer.stem(tokens[i])
                if word.isalpha() and word not in stopwords.words('english'):
                    result[word] = result.get(word,0) + 1

    print(result)
    fout = open(outfile, 'w')
    result = sorted(result.items(),key = lambda x:x[1],reverse = True)

    print('length:',len(result))

    for item in result:
        key = item[0]
        value = item[1]
        fout.write(key+','+str(value)+'\n')
    fout.close()


def statistic_verbword_spacy(outfile,rfc_file1,rfc_file2):
    result = {}

    sentences1 = get_sentences(rfc_file1)
    sentences2 = get_sentences(rfc_file2)
    sentences = sentences1 + sentences2
    count = 0
    for sent in sentences:
        count += 1
        print(count)
        # if i > 100:break
        doc = nlp(sent)
        for token in doc:
            # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            #       token.shape_, token.is_alpha, token.is_stop)
            if token.pos_ == 'VERB':
                word = token.lemma_
                if word.isalpha():    # 去停用词???
                    result[word] = result.get(word,0) + 1

    print(result)
    fout = open(outfile, 'w')
    result = sorted(result.items(),key = lambda x:x[1],reverse = True)

    print('length:',len(result))

    for item in result:
        key = item[0]
        value = item[1]
        fout.write(key+','+str(value)+'\n')
    fout.close()


def statistic_modalwords(modal_sentence_file):
    total_sent_num = 0
    modal_sent_num_dict = defaultdict(int)
    count = 0
    modal_times_dict = defaultdict(int)
    more_than_once_modal_dict = defaultdict(int)

    for line in open(modal_sentence_file,'r'):
        count += 1
        if count % 5 != 1:
            continue
        total_sent_num += 1
        line = line.strip()
        if line == '':
            continue
        # [.* SHOULD .*]	[.* MUST .*]
        line = line.replace('[.*','').replace('.*]','')
        modal_lst = [modal.strip() for modal in re.compile('\t').split(line) if modal.strip()!='']
        for modal in modal_lst:
            modal_sent_num_dict[modal] += 1
        modal_times_dict[len(modal_lst)] += 1

        if len(modal_lst) > 1:
            for modal in modal_lst:
                more_than_once_modal_dict[modal] += 1


    # 排序，输出
    modal_sent_num_dict = sorted(modal_sent_num_dict.items(), key=lambda x:x[1],reverse=True)
    print('rfc:{} 文档中共有 {} 个句子包含情态动词'.format(modal_sentence_file, total_sent_num))

    print('{word} 出现在 {num} 个句子中')
    for key,value in modal_sent_num_dict:
        print('{},{}'.format(key, value))

    print('有 {num} 个句子出现情态动词 {num} 次')
    for key,value in sorted(modal_times_dict.items(), key=lambda x:x[1], reverse=True):
        print('{},{}'.format(value, key))

    print('包含两个及以上情态动词的句子中，{} 出现 {} 次')
    for key,value in sorted(more_than_once_modal_dict.items(), key=lambda x:x[1], reverse=True):
        print('{},{}'.format(key, value))





# statistic_verbword_spacy('statistic_verb_spacy.txt','RFC2616.txt','RFC7230.txt')
# statistic_modalwords('7230_contain_capital_modal_sentences.txt')
statistic_modalwords('2616_contain_all_modal_sentences.txt')

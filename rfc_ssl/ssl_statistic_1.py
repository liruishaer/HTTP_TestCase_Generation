# -*-coding=utf-8-*-
from collections import defaultdict
MODAL_CAPITAL_WORDS = ["MUST", "SHOULD", "RECOMMENDED", "MUST NOT", "SHOULD NOT", "MAY"]

def analysis_ASN(modal_sentence_file):
	fin =  open(modal_sentence_file,'r')
	count = 0
	all_sent_num = 0
	modal_sent_num = 0
	model_dict = defaultdict(int)
	for line in fin:
		count += 1
		if count % 5 == 2:
			all_sent_num += 1
			flag = False
			for ptn in MODAL_CAPITAL_WORDS:
				if ptn in line:
					model_dict[ptn] += 1
					flag = True
			if flag == True:
				modal_sent_num += 1
	fin.close()
	print('sentence number than have modal words:',modal_sent_num)
	print('all sentence number:',all_sent_num)
	for key in model_dict:
		value = model_dict[key]
		print(key,':',value)


# contain_modal_sentence_file = '1_rfc5280_contain_modal_sentence.txt'
contain_modal_sentence_file = '1_rfc6818_contain_modal_sentence.txt'
analysis_ASN(contain_modal_sentence_file)



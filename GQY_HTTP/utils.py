#!/usr/bin/env python
# coding=utf-8

import itertools
import json

'''
utils:工具包
'''

def permutation(lst,length='ALL'):
    '''
    求列表lst中元素的排列(默认是全排列)，同时去重。
    len可取值:'ALL' 或 正整数(小于等于列表lst的长度)
    '''
    if length == 'ALL':
        length = len(lst)
    permutation_lst = list(itertools.permutations(lst,length))
    return list(set(permutation_lst))

def cartesian_product(lst):
    '''
    计算列表lst中各个子列表的迪卡尔积

    lst = [sub_lst1,sub_lst2, ... ]
    '''
    return list(itertools.product(*lst))

def load(filename):
    '''
    读取json格式的配置文件,返回一个dict
    '''
    with open(filename,'r') as f:
        conf_dict = json.load(f)
    return conf_dict

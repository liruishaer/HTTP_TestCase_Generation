#!/usr/bin/env python
# coding=utf-8

import http_request
import utils


class Generator:
    '''
    解析、生成HTTP Requst的操作类
    '''
    def __init__(self,conf_path='/home/gqy/Desktop/Http_Gengerator/Version_2/'):
        self.request = http_request.Request()   #Request类的对象
        self.conf_path = conf_path
        
    
    def conf_parse(self,conf_file):
        '''
        解析带有配置选项的文件conf_file,并给self.request的各属性赋值,如:
        * self.request.Headers
        * self.request.Request_Line
        * self.request.Line_CRLF
        * self.request.End_Line
        '''

        conf_dict = utils.load(self.conf_path+conf_file)
        '''
        conf_dict中每个key对应的value的type有三种取值情况:
        * value是字符串列表，如 "Header_Line_CRLF": ["\r\n"]
        * value是dict
        * value是dict的列表
        '''
        for key,values in conf_dict.items():
            func = getattr(self.request,key.lower())

            #key对应的值是dict
            if isinstance(values,dict):
                func(**values)
            #key对应的值是列表
            elif isinstance(values,list):
                for value in values:
                    #列表中的元素是dict
                    if isinstance(value,dict):
                        func(**value)
                    #列表中的元素不是dict，可能是数字、str或list
                    else:
                        #注意:这里不是程序解包，是位置参数
                        func(values)
                        break   
                        
                        
    def get_request(self):
        '''
        wrapper function
        返回self.request中所有可能的HTTP Request的字符串表示
        '''
        return self.request.get_request()
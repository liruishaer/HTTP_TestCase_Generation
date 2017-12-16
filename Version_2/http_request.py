#!/usr/bin/env python
# coding=utf-8

import utils

class Request:
    '''
    HTTP Request的操作类及数据结构
    '''
    
    def __init__(self):
        self.Headers = {}
        self.Request_Line = []
        self.Header_Lines = []
        self.Header_Line_CRLF = []
        self.End_Line = []
        
        
    def request_line(self,Method=['GET'],Request_URI=['/'],HTTP_Version=['HTTP/1.1'],Space=[' '],Line_CRLF=['\r\n']):
        '''
        得到该Request的所有可能的Request_Line，存入一个列表(self.Request_Line)中
        '''
        for request_line_components in utils.cartesian_product([Method,Request_URI,HTTP_Version,Space,Line_CRLF]):
            method,request_uri,http_version,space,line_crlf = request_line_components
            request_line = method + space + request_uri + space + http_version + line_crlf
            self.Request_Line.append(request_line)
            
            
    def header_line_crlf(self,header_line_crlf=['\r\n']):
        '''
        得到Header_Line中的换行符列表，存入self.Header_Line_CRLF中
        '''
        self.Header_Line_CRLF = header_line_crlf
        
        
    def end_line(self,end_line=['\r\n']):
        '''
        得到End_Line列表，存入self.End_Line中
        '''
        self.End_Line = end_line
    
    
    def header_copy(self,name='',num=0,value=[],style=[]):
        '''
        在该Request中，得到名为name的Header对应的所有value和style的组合，存入self.Headers[name]中
        '''
        #得到value的所有排列，去重
        values = utils.permutation(value)
        
        #len(style)<num的情况下，用0(表示无空格)填补
        style.extend([0]*(num-len(style)))
        #得到style的所有排列，去重
        styles = utils.permutation(style)
        
        #对values和styles求迪卡尔积
        values_and_styles = utils.cartesian_product([values,styles])
        self.Headers[name] = values_and_styles
        
      
    def header_lines(self):
        '''
        得到该Request的所有可能的Header_Line，存入一个列表(self.Header_Lines)中
        该Request中出现的所有Header对应的行都写进一个字符串，一个字符串表示一种Headers(所有Header都包括)的取值
        '''   
        header_name_lst = self.Headers.keys()
        header_info_lst = self.Headers.values()
        
        for header_line_crlf in self.Header_Line_CRLF:
            for headers_info in utils.cartesian_product(header_info_lst):
                header_line = ''
                for header_name, headers_with_same_name in zip(header_name_lst,headers_info):
                    for i in range(len(headers_with_same_name[0])):
                        header_line += self.get_single_header_line(header_name,headers_with_same_name[0][i]
                                                                  ,headers_with_same_name[1][i],header_line_crlf)
                self.Header_Lines.append(header_line)
        return self.Header_Lines
           
        
    def get_single_header_line(self,header_name,header_value,header_style,header_line_crlf):
        '''
        返回单行header_line的字符串
        以'Host'为例，根据参数不同，得到不同的结果:
        * ('Host','www.benigh.com',0,'\r\n')    ---> 'Host:www.benigh.com\r\n'
        * ('Host','www.benigh.com',-1,'\r\n')   ---> ' Host:www.benigh.com\r\n'
        * ('Host','www.benigh.com',1,'\r\n')    ---> 'Host: www.benigh.com\r\n'
        '''       
        if header_style<0:
            header_name = ' '*(0-header_style) + header_name + ':'
        else:
            header_name = header_name + ':' + ' '*header_style
        
        return header_name + header_value + header_line_crlf
    
    
    def get_request(self):
        '''
        返回该Request所有可能的字符串表示，字符串列表
        '''
        requests = []
        for request_line in self.Request_Line:
            for header_line in self.header_lines():
                for end_line in self.End_Line:
                    requests.append(request_line+header_line+end_line)
                    
        return requests
    
    
   

        
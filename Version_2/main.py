# -*- coding=utf-8 -*-
import generator

generator = generator.Generator()

grammar_conf = 'grammar.conf'       #HTTP Request的Grammar配置文件
rule_conf = 'rule.conf'             #HTTP Request的Rule配置文件

#分别解析Grammar文件和Rule文件
generator.conf_parse(grammar_conf)
generator.conf_parse(rule_conf)

#得到所有可能的HTTP Request的字符串表示
requests = generator.get_request()

for req in requests:
    print (req)



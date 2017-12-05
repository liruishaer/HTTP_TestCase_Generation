
# coding: utf-8

# In[1]:


import generator


# In[2]:


generator = generator.Generator()

grammar_conf = 'grammar.conf'       #HTTP Request的Grammar配置文件
rule_conf = 'rule.conf'             #HTTP Request的Rule配置文件


# In[7]:


#分别解析Grammar文件和Rule文件
generator.conf_parse(grammar_conf)
generator.conf_parse(rule_conf)


# In[8]:


#得到所有可能的HTTP Request的字符串表示
requests = generator.get_request()


# In[9]:


for req in requests:
    print (req)


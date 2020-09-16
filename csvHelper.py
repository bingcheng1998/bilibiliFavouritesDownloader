#!/usr/bin/env python
# coding: utf-8

# # CSV 数据存储服务
# 
# - 数据存储为csv表格，提供方法：
#     - 新建表格
#     - 增添新的行
#     - 删除行
#     - 修改行
#     - 查找行
#     - 存在行
#     
# - 用于替换sqlite，方便随时查看内容
# 
# - 用于少量数据且对于效率要求不高的应用（如爬虫）

# ## 新建表格
# 
# - 存在则查看是否形式一致，一致则跳过
# - 不一致则报错，停止
# - 不存在则新建

# In[54]:


import csv

def newCSV(title, fileds_list):
    with open(title, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fileds_list)
        writer.writeheader()
        
if __name__ == '__main__':
    fieldnames = ['first_name', 'last_name']
    title = 'names.csv'
    newCSV(title, fieldnames)


# ## 增加行

# In[56]:


def addLine(title, content_dict):
    with open(title, 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(content_dict)
        
if __name__ == '__main__':
    title = 'names.csv'
    content_dict =[ 'Baked', 'Beans']
    addLine(title, content_dict)
    dd =[ 'Baked2', 'Beans']
    addLine(title, dd)
    dd =[ 'Baked3', 'Beans']
    addLine(title, dd)
    dd =[ 'Baked4', 'Beans']
    addLine(title, dd)
        


# ## 查找行

# In[60]:


def search(title, s):
    try:
        with open(title, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if s in row:
#                     print(row)
                    return row
            return None
    except:
        return None
    
def exist(title, s):
    return search(title, s) is not None
            
if __name__ == '__main__':
    title = 'names.csv'
    s = 'Baked5'
    search(title, s)
    print(exist(title, s))
            


# In[ ]:





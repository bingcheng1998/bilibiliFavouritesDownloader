#!/usr/bin/env python
# coding: utf-8

# In[29]:


# %load_ext autoreload
# %autoreload 2


# In[30]:


def url2bv(url):
    # https://www.bilibili.com/video/BV1NJ411H7JH/ -> BV1NJ411H7JH
    bv = url.split('/')
    if len(bv[-1]) == 0:
        bv = bv[-2]
    else: bv = bv[-1]
    assert bv[:2] == 'BV'
    return bv
    
url2bv('https://www.bilibili.com/video/BV1NJ411H7JH/')


# In[44]:


import HeaderHelper as hh
from user_info import user_info
import json

def getPartNames(url, pages):
    bvid = url2bv(url)
    url, params, headers = hh.gen_fav_info(hh.LIST_PART_INFO, user_info['cookie'])
    params['bvid'] = bvid
#     print(url, params, headers)
    response = hh.send_request(url, headers, params)
    list_json = json.loads(response.text)
    # assert len(list_json['data']) == pages, (len(list_json['data']), pages)
    if len(list_json['data']) != pages:
        print("error! (len(list_json['data']), pages) = ", (len(list_json['data']), pages))
    p_name = []
    for part in list_json['data']:
        p_name.append(part['part'])
    return p_name, len(list_json['data'])


# In[36]:


import re
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "-", title)  # 替换为-
    return new_title


# In[11]:


from subprocess import call
def download(url, path, name):
#     shell_run = f"youtube-dl -o '{path}/%(title)s.%(ext)s' {url}"
    shell_run = f"you-get -o '{path}' -O '{name}'  -c ./cookies.txt {url}"
    print(shell_run)
    call(shell_run, shell=True)

def playlist(url, path, pages):
    p_name, pages = getPartNames(url, pages)
    for i in range(pages):
        print(f'开始下载 {i}/{pages}')
        shell_run = f"you-get -o '{path}' -O '[P{i+1}].{validateTitle(p_name[i])}'         -c ./cookies.txt {url}?p={i+1}"
        print(shell_run)
        call(shell_run, shell=True)


# In[12]:


if __name__ == '__main__':
#     url='https://www.bilibili.com/video/BV1NJ411H7JH'
    url = 'https://www.bilibili.com/video/BV1r4411f7td?p=5'
    pages = 60
    path = '/Users/bingcheng/Downloads/bv1'
    download(url, path, 'test2')
#     playlist(url, path, pages)


# In[ ]:





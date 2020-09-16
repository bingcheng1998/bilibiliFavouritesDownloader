#!/usr/bin/env python
# coding: utf-8

# In[1]:


# %load_ext autoreload
# %autoreload 2
import getFav
from user_info import user_info
import os
import newVideoDownloader as vd


# In[2]:


import csvHelper as csv


# In[5]:


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:        
        os.makedirs(path) 
        print(f'new path {path}')
    else:
        print(f'path `{path}` exists')


# In[6]:


import re
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "-", title)  # 替换为-
    return new_title


# In[7]:


def download(media_id):
    title = 'bilibili.csv'
    fav_title, fav_up, fav_num = getFav.getFavInfo(media_id)
    print(fav_title, fav_up, fav_num)
    path = user_info['path']
    print(f'下载位置为 `{path}`')
    fav_path = path+'/'+fav_title
    mkdir(fav_path)
    bv_list, page_list, title_list = getFav.getFavList(media_id)
    getFav.showFavInfo(title_list)
    for i in range(fav_num):
        if csv.exist(title, bv_list[i]):
            # print(f'视频 《{title_list[i]}》 已下载')
            continue
        if title_list[i] == '已失效视频':
            # print(f'视频 {title_list[i]} 已失效')
            continue
        url = f'https://www.bilibili.com/video/{bv_list[i]}'
        print(f'开始下载 《{title_list[i]}》: {url}, 共{page_list[i]}P:')
        if page_list[i] == 1:
            vd.download(url, fav_path, title_list[i])
        if page_list[i] > 1:
            vid_path = fav_path + '/' +validateTitle(title_list[i])
            mkdir(vid_path)
            vd.playlist(url, vid_path, page_list[i])
        csv.addLine(title, [bv_list[i], title_list[i], page_list[i]])


# In[ ]:


if __name__ == '__main__':
    media_id = 51460660
    download(media_id)


# In[ ]:





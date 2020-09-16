#!/usr/bin/env python
# coding: utf-8

# In[1]:


from ListDownload import download


# In[2]:


from user_info import user_info


# In[3]:


favorate_ids = user_info['favorate_id']


# In[ ]:


for media_id in favorate_ids:
    download(media_id)


# In[ ]:





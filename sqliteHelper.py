#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
from log_init import Log 
log = Log()


# In[19]:


def insertHelper(db, table, insert_dict):
    conn = sqlite3.connect(db)
    log.info(f'Opened database [{db}] successfully')
    c = conn.cursor()
    space1 = '`%s`, '*(len(insert_dict)-1) + '`%s` '
    space2 = '"%s", '*(len(insert_dict)-1) + '"%s" '
    sql = f'INSERT INTO `{table}` ({space1}) VALUES ({space2})'
    val = tuple((insert_dict.keys())) + tuple(insert_dict.values())
    log.info(sql%val)
    c.execute(sql%val)
    conn.commit()
    log.info (f"[{db}]: Records created successfully")
    conn.close()
    
def updateHelper(db, table, update_dict, constraint_dict):
    conn = sqlite3.connect(db)
    log.info(f'Opened database [{db}] successfully')
    c = conn.cursor()
    space1 = '`%s` = "%s", '*(len(update_dict)-1) + '`%s` = "%s" '
    space2 = '`%s` = "%s", '*(len(constraint_dict)-1) + '`%s` = "%s" '
    val = tuple(list(update_dict.items())[0]) + tuple(list(constraint_dict.items())[0])
    sql = f'UPDATE `{table}` SET {space1} where {space2}'
    log.info(sql%val)
    c.execute(sql%val)
    conn.commit()
    log.info (f"[{db}]: Records updated successfully")
    conn.close()
    
def getHelper(db, table, items, constraint_dict):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    log.info(f'Opened database [{db}] successfully')
    space1 = '`%s`, '*(len(items)-1) + '`%s` '
    space2 = '`%s` = "%s", '*(len(constraint_dict)-1) + '`%s` = "%s" '
    val = tuple(items)+tuple(list(constraint_dict.items())[0])
    sql = f"SELECT {space1} from {table} where {space2}"
    log.info(sql%val)
    cursor = c.execute(sql%val)
    answer = []
    for row in cursor:
        s_answer = []
        for r in row:
            s_answer.append(r)
        answer.append(s_answer)

    log.info(f"[{db}]: Operation done successfully")
    conn.close()
    return answer
    
def truncateTable(db, table):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    sql = 'DELETE FROM `'+table+'`;'
    try:
        cursor.execute(sql)
        cursor.connection.commit()
        log.info('Delete all lines from table ['+table+'] - [success!]')
    except BaseException as e:
        log.warning(e)
        log.warning(sql+' - [Failed]')
        cursor.connection.rollback()
    cursor.close()
    conn.close()


# In[20]:


if __name__ == '__main__':
    table_name = 'test.sqlite3'
    truncateTable(table_name, 'nhentai')
    tags_list = '27445 108086 86951 86952 14283 21712 13720 23895 123812 33172 6346'
    insert_dict = {'manga_id': '1020', 'tags_list': tags_list}
    insertHelper(table_name, 'nhentai', insert_dict)
    updateHelper(table_name, 'nhentai', {'tags_list': tags_list}, {'manga_id': '102'})
    answer = getHelper(table_name, 'nhentai', ['tags_list', 'manga_id'], {'manga_id': 1020})
    print('len =',len(answer),answer)


# In[ ]:





# In[ ]:





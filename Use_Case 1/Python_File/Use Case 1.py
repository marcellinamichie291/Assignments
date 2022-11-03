#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mysql-connector-python


# # Birds table

# In[9]:


import mysql.connector
import pandas as pd
import numpy as np

hostname = 'localhost'
database = 'use_case'
username = 'root'
pwd = 'root'
port_id = 3306
conn = None
cur = None

try:
    conn = mysql.connector.connect(host = hostname,
                            database = database,
                            user = username,
                            password = pwd,
                            port = port_id)

    cur = conn.cursor()
    
    cur.execute('SELECT * FROM Birds')
    data = cur.fetchall()
    #print(data)
    birds_table = pd.DataFrame(data, columns=['ID','BirdName','TypeOfBird','ScientificName'])
    print(birds_table)
    
    birds_table.to_csv('C://Users//chaithra.chandru//Desktop//birds_csv.csv')
    
    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


# # Books table

# In[1]:


import mysql.connector
import pandas as pd
import numpy as np

hostname = 'localhost'
database = 'use_case'
username = 'root'
pwd = 'root'
port_id = 3306
conn = None
cur = None

try:
    conn = mysql.connector.connect(host = hostname,
                            database = database,
                            user = username,
                            password = pwd,
                            port = port_id)

    cur = conn.cursor()
    
    cur.execute('SELECT * FROM Books')
    book_data = cur.fetchall()
    #print(data)
    books_table = pd.DataFrame(book_data, columns=['BookName', 'Category', 'Price', 'Price_Range'])
    #print(books_table)
    
    books_pivot = pd.pivot_table(books_table, index=['Category', 'Price_Range'], values=['Price'], aggfunc=np.sum)
    print(books_pivot)
    
    books_pivot.to_csv('C://Users//chaithra.chandru//Desktop//book_pivot_csv.csv')
    
    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


# In[2]:


import mysql.connector
import pandas as pd
import numpy as np

hostname = 'localhost'
database = 'use_case'
username = 'root'
pwd = 'root'
port_id = 3306
conn = None
cur = None

try:
    conn = mysql.connector.connect(host = hostname,
                            database = database,
                            user = username,
                            password = pwd,
                            port = port_id)

    cur = conn.cursor()
    
    cur.execute('SELECT * FROM Books')
    book_data = cur.fetchall()
    #print(data)
    books_table = pd.DataFrame(book_data, columns=['BookName', 'Category', 'Price', 'Price_Range'])
    #print(books_table)
    
    books_pivot = pd.pivot_table(books_table, index=['Category'], values=['Price'], aggfunc=np.sum)
    print(books_pivot)
    
    books_pivot.to_csv('C://Users//chaithra.chandru//Desktop//books_pivot_csv.csv')
    
    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import numpy as np

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',  
'londON_StockhOlm', 
'Budapest_PaRis', 'Brussels_londOn'], 
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085], 
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]], 
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )', 
'12. Air France', '"Swiss Air"']}) 

df.head()


# In[5]:


df.columns


# In[9]:


df.dtypes


# In[22]:


df['From_To']

m = [char.lower() for char in df['From_To']]

ls = pd.Series(m)
df['From_To'] = ls
df.head()


# #### 1. Some values in the the FlightNumber column are missing. These numbers are  meant to increase by 10 with each row so 10055 and 10075 need to be put in  place. Fill in these missing numbers and make the column an integer column  (instead of a float column). 

# In[29]:


for i in range(4):
   if pd.isnull(df['FlightNumber'][i]) == True:
       df['FlightNumber'][i] = df['FlightNumber'][i-1] + 10
df.head()  


# #### 2. The From_To column would be better as two separate columns! Split each  string on the underscore delimiter _ to give a new temporary DataFrame with  the correct values. Assign the correct column names to this temporary  DataFrame. 

# In[30]:


tempo = df.copy()
tempo


# In[31]:


m = [tempo['From_To']]
lst = [m[0][i] for i in range(len(tempo['From_To'] )) ]
  

lst2 = [i.split('_') for i in lst]

lst3 = [lst2[i][j] for i in range(len(lst2)) for j in range(1)]
lst4 = [lst2[i][k] for i in range(len(lst2)) for j in range(1) ]

lst5 = [i for i in lst4]

lst5  


# In[32]:


tempo['From'] = pd.Series(lst3)
tempo['To'] = pd.Series(lst5)
tempo.head()


# #### 3. Notice how the capitalisation of the city names is all mixed up in this  temporary DataFrame. Standardise the strings so that only the first letter is  uppercase (e.g. "londON" should become "London".) 

# In[35]:


tempo['From'] = tempo['From'].str.capitalize()
tempo['To'] = tempo['To'].str.capitalize()
tempo


# #### 3. 4. Delete the From_To column from df and attach the temporary DataFrame  from the previous questions. 

# In[39]:


df.drop('From_To', axis = 1, inplace = True)
df


# In[40]:


df['From'] = tempo['From']
df['To'] = tempo['To']
df


# #### 5. In the RecentDelays column, the values have been entered into the  DataFrame as a list. We would like each first value in its own column, each second value in its own column, and so on. If there isn't an Nth value, the value  should be NaN. Expand the Series of lists into a DataFrame named delays, rename the columns  delay_1, delay_2, etc. and replace the unwanted RecentDelays column in df  with delays. 
# 

# In[70]:


dela = df['RecentDelays']


# In[ ]:





# In[ ]:





# In[71]:


df3 = pd.DataFrame(df['RecentDelays'].values.tolist())


# In[72]:


df3


# In[73]:


dic = {}
val = []
for i in range(3):
    key = i
    values = 'Delay'+ str(i+1)
    val.append(values)
    dic[key] = values
dic    
    
#p = pd.Series(dic)    
df3.rename(columns = dic, inplace = True)
df3


# In[68]:


df.join(df3)


# In[ ]:





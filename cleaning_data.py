#!/usr/bin/env python
# coding: utf-8

# # Import Packages and set up dataframe

# In[1]:


import pandas as pd
import numpy as np


# Set the number of decimal places in the dataframe

# In[2]:


pd.set_option("display.precision", 2)


# Read the Training data

# In[3]:


df = pd.read_csv("train.csv")


# To review the data in the dataframe

# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.isna().any()


# # To clean the data

# Drop columns if there is too little value or of the information repeats

# In[8]:


todrop = ['Capillary refill rate', 
          'Glascow coma scale eye opening', 
          'Glascow coma scale motor response', 
          'Glascow coma scale motor response', 
          'Glascow coma scale verbal response' ]


df = df.drop(columns=todrop)


# In[9]:


#List of columns
list(df.columns.values)

for column in list(df.columns.values)[1: -1]:
    #Median
    median = df[column].median()

    #IQR
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    #getting df of outliers 
    outliers = (df[column] - median).abs() > 1 * IQR

    #replace outliers with nan
    df.loc[outliers, column] = np.nan
    
    #replace nan with median
    df[column]=df[column].fillna(median)


# In[10]:


df.to_csv("cleaned.csv")


# To check if all data is available

# In[11]:


df.isna().any()


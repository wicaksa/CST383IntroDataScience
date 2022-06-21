# Wicaksa Munajat
# 05/20/2022
# CST383 Summer '22

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


#@ 1. Create an Python file in Spyder, and enter this code to read the data:


# In[3]:


infile = "https://raw.githubusercontent.com/grbruns/cst383/master/campaign-ca-2016-sample.csv"
df = pd.read_csv(infile)


#  Record your work on the following problems in your Python file.

# In[4]:


#@ 2. Look at some of the data using the variable explorer in the upper right pane of Spyder. (Select the 'Variable explorer' tab and double click on 'df'.)


# In[5]:


df.info()
df.head(20)


# In[6]:


#@ 3. Look at the type of each column in df.  (We'll sometimes refer to the columns as 'variables', 'attributes', or 'features'.)  How many columns are shown as numeric?  Do you think some of the columns should be numeric but aren't?


# In[7]:


# There are 2 columns shown as numeric (contb_receipt_amt, and file_num).
# I think the cand_id, cand_id, contbr_zip should all be type int64.


# In[8]:


#@4. Which of the columns contain NA values?  
#### Use Python to figure out the total number of NA values in the data set.  


# In[9]:


# Columns with NA values include: contbr_employer, receipt_desc, memo_cd, memo_text.
# Total number of NA values: 52563
df.isna().sum().sum()


# In[10]:


#@5. Can you find values (besides 'nan') that indicate missing data?  
#### You can try doing this with Python or by searching manually through df.  
#### High-level hint: you might expect an NA value in a column to appear many times.


# In[11]:


# Try df.contbr_occupation.value_counts().head(n=20)   
# This will show the 20 most common values in the column 'contbr_occupation'.  
# Look carefully at the values -- do any of them seem to indicate missing data?
df.contbr_occupation.value_counts().head(n=20)
# Some missing data include in the contbr_occupation column: INFORMATION REQUESTED PER BEST EFFORTS, NONE, INFORMATION REQUESTED.
# You can use value_counts() to get the summary of the column. From there, you can see which data looks like they might be incomplete.


# In[12]:


#@ 6. Does missing data exist in attribute contbr_employer?  
#### If so, how is it encoded?  Would it make sense to change it?
#### Yes, there are values such as NONE, REFUSED, INFORMATION REQUESTED PER BEST EFFORTS, AND INFORMATION REQUESTED.
#### I think it would make sense to change it to one category.
df.contbr_employer.value_counts().head(n=20)
"""
RETIRED                                   3419
NOT EMPLOYED                              2305
SELF-EMPLOYED                             1206
SELF                                      1057
SELF EMPLOYED                              625
NONE                                       606
INFORMATION REQUESTED PER BEST EFFORTS     342
INFORMATION REQUESTED                      249
HOMEMAKER                                  207
STATE OF CALIFORNIA                         84
GOOGLE                                      60
KAISER PERMANENTE                           59
STANFORD UNIVERSITY                         37
UNIVERSITY OF CALIFORNIA                    37
APPLE                                       31
LOS ANGELES COUNTY                          30
UCLA                                        29
LAUSD                                       24
APPLE INC.                                  23
MR.                                         23
UNITED AIRLINES                             21
UC BERKELEY                                 21
UNEMPLOYED                                  21
HILLARY FOR AMERICA                         21
SYNOPSYS                                    19
UNIVERSITY OF SOUTHERN CALIFORNIA           18
FACEBOOK                                    17
MS.                                         16
CITY OF LOS ANGELES                         16
WELLS FARGO                                 16
STUDENT                                     16
REFUSED                                     15
UCSF                                        15
LOS ANGELES UNIFIED SCHOOL DISTRICT         14
FREELANCE                                   14
UNITED STATES NAVY                          14
SUTTER HEALTH                               13
SONOMA STATE                                13
UC DAVIS                                    13
AT&T                                        11
SALESFORCE                                  11
UC SAN DIEGO                                11
UNIVERSITY OF CALIFORNIA, DAVIS             11
RAYTHEON                                    11
LOCKHEED MARTIN                             11
USPS                                        11
CALIFORNIA NURSES ASSOCIATION               10
US NAVY                                     10
STATE OF CA                                 10
BANK OF AMERICA                             10
Name: contbr_employer, dtype: int64

"""


# In[13]:


#@7. Look more at contbr_employer.  Do you see any other data quality issues?
#### There are more than one INFORMATION REQUESTED PER BEST EFFORTS and INFORMATION REQUESTED. 
#### Also, you have SELF-EPLOYED, SELF EMPLOYED, AND SELF which may mean the same thing.


# In[14]:


#@8. How many different values are there in attribute ‘memo_cd’?  
#### What are the values?  What fraction of the values are empty? 
#### There are 20,000 different values.

df['memo_cd']
"""
0        NaN
1        NaN
2        NaN
3        NaN
4        NaN
        ... 
19995    NaN
19996    NaN
19997    NaN
19998    NaN
19999    NaN
Name: memo_cd, Length: 20000, dtype: object
"""

df['memo_cd'].isnull().sum()
"""
19381
"""

np.divide(df['memo_cd'].isnull().sum(), 20000)
"""
0.96905
"""


# In[15]:


#@9. Attribute ‘contb_receipt_amt’ is the amount of the contribution.  
#### Produce a histogram of the values.  
#### Be sure your plot has a good title and good axis labels.
ax = df['contb_receipt_amt'].plot(kind='hist', title='Amount of Money People Contributed')
ax.set_xlabel("Amount Contributed in Dollars")
ax.set_ylabel("Number of People")
ax.set_xlim(-5500, 11000)


# In[16]:


#@10. What is the range of ‘contb_receipt_amt’ values?  Do any of them look suspicious?  
#### How should you deal with negative campaign contributions?  
#### Do negative contributions tend to be paired with positive contributions?
#### The range is -5400 to 10800. Maybe the negative contribution was an error and it should have been positive. 
#### We should change it to positive. 

df.describe()
"""
    	contb_receipt_amt 	file_num
count 	20000.000000 	2.000000e+04
mean 	272.404752 	1.042429e+06
std 	738.984362 	1.018850e+04
min 	-5400.000000 	1.003942e+06
25% 	25.000000 	1.032443e+06
50% 	50.000000 	1.046975e+06
75% 	100.000000 	1.051507e+06
max 	10800.000000 	1.051624e+06
"""


# In[17]:


#@11. Attribute contbr_zip has the zip code of a contributor.  
#### Are all zip codes in the same format?  
#### If not, do you think it would be appropriate to process the zip code data?
#### The Zip codes show 9 digits and 5 digits. 
#### I think you can process it to just show the first 5 or 9 digits. 

df['contbr_zip'].value_counts()
"""
951241559    16
941311708    14
954039414    13
926483765    12
943061338    12
             ..
931013664     1
934609751     1
906317778     1
958183621     1
954489434     1
Name: contbr_zip, Length: 13710, dtype: int64
"""

x = df['contbr_zip']
x.str.len().value_counts()
"""
9    19402
5      598
Name: contbr_zip, dtype: int64
"""


# In[18]:


#@12. Create a histogram of the lengths of contbr_employer values (i.e., the length of the values as strings).  
#### Is the distribution unusual?  
#### Give an explanation, based on working with the data, of why some employer length values seem to be very popular.
#### Not unusual. It just means there is one company that a lot of the people work for.

gr = df['contbr_employer'].str.len().value_counts().plot(kind='hist', title='Length of contbr_employer Values')
gr.set_xlabel("Number of Employers")
gr.set_ylabel("Length")


# In[19]:


#@13. If we scale a vector of numeric values using 0-1 scaling, then the smallest value in the vector will become 0, the largest will become 1, and the others will be scaled linearly between 0 and 1.  
#### Create a new attribute, s_amt1, from ‘contb_receipt_amt’ by using 0-1 scaling. 
df['s_amt'] = df['contb_receipt_amt']/df['contb_receipt_amt'].max()


# In[20]:


#@14. What do memo_cd values mean?  
#### How do they relate to the values in ‘memo_text’?  
#### Note: an "earmarked" contribution is one that's not given directly to a candidate but marked to indicate the candidate to which the contribution will be given.
#### Some 'memo_text' has an 'X' and a memo_text corresponding to the person's campaign.
#### It looks like it's a way of telling you if they contributed directly to a campaign.


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Create a new Python program in Spyder (or create a notebook if you prefer), and add the following imports:  
# (feel free to copy and paste this)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


# In[2]:


# 2. Enter this code to load the College data
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv',index_col=0)


# In[3]:


# 3. How would you get an overview of the data?
df.info()


# In[4]:


#4. We will try to predict whether a college is public or private using the cost of tuition and the number of full-time students.  
# Use this code from the lecture to convert the data to NumPy, split it into test and training sets, and scale. 


# In[5]:


X = df[['Outstate', 'F.Undergrad']].values
y = (df['Private'] == 'Yes').values.astype(int) # Private = 1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# In[7]:


# 5. Print the first 10 rows of X_train to make sure the data is scaled.
X_train


# In[8]:


# 6. Build a KNN classifier and train it.  Use the default value of k (which is parameter n_neighbors KNeighborsClassifier).  
# See lecture slides.

clf = KNeighborsClassifier()
clf.fit(X_train, y_train)


# In[9]:


# 7. Make predictions using the training set, and save the predictions as variable 'predictions'.
predictions = clf.predict(X_test)


# In[11]:


# 8. Compare the first ten predictions with the first ten correct (test set) values.
print(predictions[:10])
print(y_test[:10])


# In[12]:


# 9. Which two variables do you need to compute the accuracy of your classifier on the test set?
# Predictions and y_test


# In[13]:


# 10. Compute and print the test set accuracy of your classifier.


# In[ ]:


accuracy = (predictions == y_test).mean()


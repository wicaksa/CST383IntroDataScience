#!/usr/bin/env python
# coding: utf-8

# In[1]:


# kNN regression is very similar to kNN classification. Try to solve each problem without using hints.


# In[2]:


# I highly recommend that you not copy and paste code, but instead type it in yourself.  This will help your learning.


# In[3]:


# 1. Create a new Python program in Spyder (or create a Jupyter notebook if you prefer), and add the following imports:  (feel free to copy and paste this)


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor


# In[5]:


# 2. Enter this code to load the College data


# In[6]:


df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv',index_col=0)


# In[7]:


# 3. We will try to predict whether the tuition of a college based on the number of students from the top 10 percent of their high school class and the number of undergraduates.
# Create a 2D NumPy array X from the 'Top10perc' and 'F.Undergrad' columns of df. 


# In[8]:


predictors = ['Top10perc', 'F.Undergrad']
X = df[predictors].values


# In[9]:


# 4. Create a 1D NumPy array y from the 'Outstate' column of df.


# In[10]:


target = 'Outstate'
y = df[target].values


# In[11]:


# 5. Split the data into training and test sets, with 30% of the data in the test set.  
# Use names X_train, y_train, X_test, y_test.


# In[12]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 0)


# In[13]:


# 6. Now let's scale the values of the data.  
# It's important that we split that data before scaling.  
# We want to scale the training data and the test data based on the values in the training data.  
# By default, the StandardScaler class uses z-score normalization.


# In[14]:


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
x_test = scaler.transform(X_test)


# In[15]:


#7. Build a KNN regressor and train it.  
# Use the default value of k (which is parameter n_neighbors KNeighborsRegressor).


# In[16]:


regr = KNeighborsRegressor()


# In[17]:


regr.fit(X_train, y_train)


# In[18]:


# 8. Make predictions using the training set, and save the predictions as variable 'predictions'.


# In[19]:


predictions = regr.predict(X_test)


# In[20]:


# 9. Compare the first ten predictions with the first ten correct (test set) values.


# In[21]:


print(predictions[:10])
print(y_test[:10])


# In[22]:


# 10. Which two variables do you need to compute the mean squared error of your classifier on the test set?
# 1). Predictions and y_test


# In[23]:


# 11. Compute and print the mean squared error of your regressor.


# In[24]:


# 12. What MSE would you get if you always just used the average value of y_train as your prediction?  This is called a "blind prediction" because, when predicting tuition, it doesn't look at the values for Top10perc and F.Undergrad.


# In[25]:


mse_blind = ((y_train.mean() - y_test)**2).mean()
print('blind MSE: {0:.0f}'.format(mse_blind))


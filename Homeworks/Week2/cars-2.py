#!/usr/bin/env python
# coding: utf-8

# # -*- coding: utf-8 -*-
# """
#
# Using Pandas Series.
#
# In this assignment we use Pandas to study a data set about
# cars that comes from a 1974 Motor Trend magazine.
#
# Please see
# https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html
# for details about what the columns mean.
#
# Note that the displacement of an engine relates to the size and power
# of an engine.  It represents the total amount of volume the
# cylinders of the engine displace as they more.
#
# """

# """PLEASE NOTE:
#
# PLEASE NOTE: your code will be graded automatically so please
# follow these instructions carefully.
#
# Each problem line starts with #@ and is followed by a problem number.
# The problem is described on the comment lines after the problem line.
# Please insert your code just after the last comment line for the problem.
#
# My grading script grades each of your answers *independently*.  In
# other words, I do not run all of your submitted code in order.  I take
# your code for one problem, and run it in an environment where certain
# variables or functions are defined, which may include the correct
# answers to earlier problems.
#
# This means that your code for one problem should not depend on code
# for earlier problems, unless in the earlier problem you defined
# a variable or function as the answer to the earlier problem.
#
# In this assignment, each problem requires just one line of code.
# Do not use any print or assignment statements.
#
# Note that if you select a column of a Pandas DataFrame
# (for example, with df['mpg']), the type of value you get is a Pandas
# Series.
#
# """

# note: do not import other packages; my test script uses only these
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

#
# read the data
#

df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/mtcars.csv")
#@ 1
# What was the average MPG of cars like back in 1974?
# Do you think it was a lot lower than now?
# Compute the average value of the mpg series.
# Enter your code on the line immediately below this line.
df['mpg'].mean()

#@ 2
# What was the best MPG among these 1974 cars?
# Compute the maximum value of the mpg column.
df['mpg'].max()

#@ 3
# How many different numbers of forward gears did the cars in this
# dataset have?
# Compute the counts for each of the unique values in the 'gear' column.
df['gear'].value_counts()

#@ 4
# Do many cars have MPG that is greater than 20 MPG?
# Compute a Series containing the MPG values greater than 20.
# hint: use a boolean mask

# Create a series from dataframe
x = df['mpg']

# # Select all rows where data > 20 MPG
x[x > 20]

#@ 5
# What fraction of the cars have an MPG higher than 22 MPG?
# Compute a value between 0 and 1 giving the fraction of the
# cars with MPG greater than 22.
# hint: use x.size to get the number of elements in a series x

# Create a series from dataframe
x = df['mpg']

# Calculate cars with mpg > 22
x[x > 22].size / x.size

#@ 6
# Do many cars have MPG values that are within 20% of the top MPG value?
# Compute a Series containing the MPG values that are greater than
# 0.8 times the maximum MPG value in the data set.
# Hint: again, use a boolean mask.  To create the mask you'll
# need the max value of the MPG column.

# Create a series from dataframe
x = df['mpg']

# Select all rows where data > 20 MPG
x[x > 0.8 * x.max()]

#@ 7
# What are the 1/4 mile times for the cars with high MPG values?
# Compute a Series containing the qsec values for the cars that
# have MPG values greater than 0.8 times the maximum MPG value
# in the data set.
# Hint: you can use the same boolean mask you used in the last
# problem, but this time use it with the Series of the qsec
# column values.

# Create a series from dataframe for mpg
x = df['mpg']

# Create a series for 'qsec'
y = df['qsec']

# Apply the mask for x > 80% of max mpg
y[x > 0.8 * x.max()]

#@ 8
# Are the gas guzzlers a lot faster than the high MPG cars?
# Compute a Series containing the qsec values for the cars that
# have MPG values less than 1.2 times the minimum MPG value
# in the data set.

# Create a series from dataframe for mpg
x = df['mpg']

# Create a series for 'qsec'
y = df['qsec']

y[x < 1.2 * x.min()]

#@ 9
# Do cars with a small number of forward gears have high MPG?
# Compute a Series containing values in the mpg column for which the value in the 'gear' column is 3
# hint: index into a series of the mpg values using a boolean mask based on a series of the gear values

# Create a series from dataframe for mpg
x = df['mpg']

# Create a series for 'gear'
y = df['gear']

# Series showing values in the mpg column where 'gear' value is 3
x[y == 3]

#@ 10
# What about cars with a large number of forward gears?
# Compute a Series containing values in the mpg column for which the value in the 'gear' column is 5

# Create a series from dataframe for mpg
x = df['mpg']

# Create a series for 'gear'
y = df['gear']

# Series showing values in the mpg column where 'gear' value is 5
x[y == 5]

#@ 11
# On average, what's the MPG for cars with 3 forward gears?
# Compute the average value of the mpg values for which the corresponding 'gear' value is 3

# Create Series for 'mpg' column
x = df['mpg']

# Create Series for 'gear column'
y = df['gear']

# Find the average for cars 'mpg' w/ gear value == 3
x[y == 3].mean()

#@ 12
# On average, what's the MPG for cars with 5 forward gears?
# Compute the average value of the mpg values for which the corresponding 'gear' value is 5

# Create Series for 'mpg' column
x = df['mpg']

# Create Series for 'gear column'
y = df['gear']

# Find the average for cars 'mpg' w/ gear value == 5
x[y == 5].mean()

#@ 13
# Are lighter cars faster?
# Compute the average 1/4 mile time for cars with greater than average weight.

# Calculate average value for wt column
avg_wt = df['wt'].mean()

# Create a series for 'wt'
x = df['wt']

# Create a series of 'qsec'
y = df['qsec']

# Find the average of Series 'qsec' where 'wt' > avg_wt
y[x > avg_wt].mean()


#@ 14
# Now compare with the speed of lighter cars.
# Compute the average 1/4 mile time for cars with less than average weight.

# Calculate average value for wt column
avg_wt = df['wt'].mean()

# Create a series for 'wt'
x = df['wt']

# Create a series of 'qsec'
y = df['qsec']

# Find the average of Series 'qsec' where 'wt' < avg_wt
y[x < avg_wt].mean()

#@ 15
# Is there a big difference in power between cars with V6 and V8 engines?
# Calculate the average hp value for cars where vs is 0 and cyl is 8.

# Series of 'hp'
x = df['hp']

# Series of 'vs'
y = df['vs']

# Series of 'cyl'
z = df['cyl']

# Series of where vs is 0 and cyl is 8
x[(y == 0) & (z == 8)].mean()

#@ 16
# For comparison, what's the power for cars with V6 engines?
# Calculate the average hp value for cars where vs is 0 and cyl is 6.

# Series of 'hp'
x = df['hp']

# Series of 'vs'
y = df['vs']

# Series of 'cyl'
z = df['cyl']

# Series of where vs is 0 and cyl is 6
x[(y == 0) & (z == 6)].mean()

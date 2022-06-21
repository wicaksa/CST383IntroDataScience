## Purpose.  
In machine learning, it's helpful to test algorithms with simulated data.  If you do this, you can see how an algorithm's behavior changes when you change the input data.  The purpose of this assignment is to give you experience with creating simulated data and to improve your knowledge of probability and Bayes' Law, which is very important in data science.

## Instructions.  
1. Suppose 1% of people have measles, the test for measles is 98% accurate if you do have measles, and 98% accurate if you don't have measles. Then what is the probability that you have measles, given that you have tested positive for them?
2. Guess the answer to this question before you start working on this assignment.
3. We will answer this question in two ways: with a simulation, and with Bayes' Law.

## Download measles.py Download measles.py .  
1. Enter your code after each problem line.
2. Instructions are given at the top of the file.  
3. You can compare your answers with sample-output attached below. 

## In the second half of the assignment, you are asked to write a function that computes an answer based on Bayes' Law. 
1. Here is Bayes' Law applied to the problem of computing the probability of a condition being true given the test result is positive.  
2. Random variable C represents whether the condition is present.  Value 1 means it is present; 0 means it isn't present.  
3. Random variable T represents the test outcome.  Value 1 means the test was positive (in other words, showed the condition is present); 0 means the test was negative.

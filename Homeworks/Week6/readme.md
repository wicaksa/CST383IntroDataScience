# Experiments with KNN regression

## Purpose.  
The purpose of this assignment is to give you first-hand experience with how KNN regression is affected by factors like the value of k, the choice of distance function, and whether data has been scaled.

## Instructions.  
Please read the top of file knn_experiments_housing_student_X22.ipynb Download knn_experiments_housing_student_X22.ipynb .  Then edit the file following the instructions.  
Refer to knn_experiments_housing_student_S22.pdf to see some of the output of my completed version of the notebook.  I did not include all output because I want you to enjoy seeing the output of each experiment without any spoilers. Please look carefully and think about the plots you produce!

## Hints on computing training and test RMSE values.  
When using regression it is common to compute RMSE on the training set and RMSE on the test set.  Here is the process:
1. Train your regression algorithm on the training data  (X_train, y_train)
2. Compute the error on the training set:  (training RMSE)
3. Make predictions (using the trained algorithm) on X_train
4. Compute the RMSE by comparing these predictions to y_train
5. Compute the error on the test set:    (test RMSE)
6. Make predictions (using the same trained algorithm) on X_test
7. Compute the RMSE by comparing these predictions to y_test

## The test RMSE is more important than the training RMSE.  
You expect the test RMSE to be low because you are evaluating your algorithm on the same data you used to train it.  The test RMSE reflects how well your algorithm will do on data it has never seen before.

## Submission. 
You need to upload two copies of your work: the code and its pdf.
1. First, submit your edited knn_experiments_housing_student.ipynb with all of the output showing.  
2. Make sure the whole notebook runs without errors before submitting it.  (In a Jupyter notebook, select 'Run All' from the 'Cell' menu to run your entire notebook).  
3. Also, make sure that all output is displayed in your notebook before submitting it.
4. You should also submit a PDF of your notebook. You can use your browser to print the notebook as a PDF. 
5. If you are using Google Colab, to save Colab file as a PDF, select File in your browser -> Print and then save as a PDF. If you are using the Jupyter app, say in Google Chrome, click 'Open PDF in Preview' as shown here (Links to an external site.). 

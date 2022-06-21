# Exploration of the Campaign Contribution Data

## Purpose 
The purpose of this assignment is to provide a way for you to develop your skills in exploring and visualizing data.  You can use Google Colab or Jupyter notebooks.

## Instructions  
Download campaign-exploration.ipynb Download campaign-exploration.ipynb .  This is a Jupyter notebook that contains problem cells in which you are to enter your own code.  
The file campaign-exploration - kdeplot.pdf shows the output for my code (there are 2 more solution examples at the end, all eligible for full credit). 

You should attempt to create an output that looks similar to the output of one of these examples.  Be sure to use meaningful titles and axis labels. However, there are multiple plot options that are valid but may result in different visuals, due to different default values (for binning, smoothing, etc.) and we will keep that in mind while grading.
The notebook contains all packages you are to use -- do not import any other packages.

## Submission
You need to upload two copies of your work: the code and its pdf.
First, submit your edited campaign-contribution.ipynb with all of the output showing.  Make sure the whole notebook runs without errors before submitting it.  (In a Jupyter notebook, select 'Run All' from the 'Cell' menu to run your entire notebook).  Also, make sure that all output is displayed in your notebook before submitting it.
You should also submit a PDF of your notebook with all of the output displayed. If you are using Google Colab, to save Colab file as a PDF, select File > Print in your browser (not in Colab) and then save as PDF. For example, in Google Chrome, click 'Open PDF in Preview' as shown here (Links to an external site.).

Note: sns.distplot() should yield the closest look for questions asking for a "double density plot". This library is, unfortunately, being depreciated. Your choices are:
- Ignore the warning and use distplot()
    + Your plots may still look a little different than mine. Here is another solution notebook using the same code with a different version of these libraries. Notice that some of the plots are smoother. Both are eligible for full credit.

- You can experiment with the newer libraries: You can use displot() with the 'bins' parameter or kdeplot() or histplot(). Here is a submission example with these newer libraries. Also eligible for full credit.

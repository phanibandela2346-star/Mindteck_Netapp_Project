#1. Download a finance dataset CSV
#Find and save a file like 'finance.csv' from a site such as corgis-edu.github.io.

#2. Clean the data
#Use Pandas and NumPy to clean:

#Remove duplicate rows

#Fill in missing values with zero

#Make sure columns use numbers (not words)

import pandas as pd
import numpy as np

df = pd.read_csv('finance.csv')
df = df.drop_duplicates()
df = df.fillna(0)

##Visualize finance data
##Use Matplotlib to make a simple graph, for example, showing average revenue and expenditure by year:

import matplotlib.pyplot as plt

grouped = df.groupby('Year')[['Totals.Revenue', 'Totals.Expenditure']].mean()
grouped.plot()
plt.show()

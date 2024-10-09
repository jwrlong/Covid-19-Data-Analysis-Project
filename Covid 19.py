# Data Science Project - Covid 19 Data Analysis Project
# Youtube Video Link: https://www.youtube.com/watch?v=mKSWAlvXSmw


#IMPORTING LIBRARIES
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import os

#FINDING MY FILE DIRECTORY
# Get the current working directory
current_dir = os.getcwd()

# # Specify the file name
# file_name = 'your_file.txt'

# # Get the full path
# full_path = os.path.join(current_dir, file_name)

# print(f"The full path to the file is: {full_path}")


# #PRELIMINARY ANALYSIS
# data = pd.read_csv(r) #importing columns
# data.head() #we are looking at the first few observations
# data.columns()#this will allow us to see the variable names
# data.tail() #we are looking at the last few observations
# data.describe() #this will allow us to look at descriptive stats like mean, count, std
# data.isnull().sum() #this is a great way of identifying whether your dataset has null values

# #VISUALIZING RELATIONSHIPS
# #relating the variables with scatterplots
# sns.relplot(x= "variablename", y="variablename", data=data)

# sns.relplot(x= "variablename", y="variablename", data=data)

# sns.relplot(x= "variablename", y="variablename", data=data)

# sns.relplot(x= "variablename", y="variablename", hue="variablename", data=data)


# sns.pairplot(data)#this will give you a plot of the relationship between each variable as a scatterplot

# #relating the variables with linegraphs
# sns.relplot(x='variablename', y='variablename', kind='line', data=data)

# #the following will depict a scatterplot between a categorical variable and a conintuous outcome
# sns.catplot(x='recovered', y='total_cases', data=data)
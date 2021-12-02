# Basic Operation
import pandas as pd
import numpy as np

# Text Preprocessing & Cleaning
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import re


from sklearn.model_selection import train_test_split # Split Data 
from imblearn.over_sampling import SMOTE # Handling Imbalanced

# Model Building
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC


from sklearn.metrics import classification_report , confusion_matrix , accuracy_score # Performance Metrics  


# Data Visualization 
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from termcolor import cprint
import seaborn as sns
import warnings   

import os

df = pd.read_csv('data/Tweets.csv')
cprint("This is the dataset: \n",'green')
print(df.head())
cprint("\nShape of the data: ",'green')
print(df.shape)

cprint("\nTotal number of null values in the dataset: ", 'green')
print(df.isnull().sum())

##print(df.airline_sentiment.value_counts()[0])  ## for negative
##print(df.airline_sentiment.value_counts()[1])  ## for neutral
##print(df.airline_sentiment.value_counts()[2])  ## for positive


cprint("\nTotal number of tweets for each airline :",'green')
print(df.groupby('airline')['airline_sentiment'].count())

cprint('\nReasons Of Negative Tweets :','green')
print(df.negativereason.value_counts())

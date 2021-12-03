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

def convert_Sentiment(sentiment):
    if sentiment == "positive":
        return 2
    elif sentiment == "neutral":
        return 1
    elif sentiment == "negative":
        return 0

'''
    Remove URLs
'''
def remove_URLs(tweetData):
    url = re.complie(r'https?://\S+|www\.\S+')
    return url.sub(r'',tweetData)

'''
    Remove stop words
'''

def remove_stopwords(text):
    text = ' '.join([word for word in text.split() if word not in (stopwords.words('english'))])
    return text

'''
    Remove HTML tags
'''

def remove_html(text):
    temp = re.compile(r'<.*?>')
    return temp.sub(r'',temp)

'''
    Remove punctuations
'''
def remove_punctuations(text):
    temp = str.translate('','',string.punctuation)
    return text.translate(temp)

'''
    Remove @username
'''
def remove_username(text):
    return re.sub('@[^\s]+','',text)

'''
    Remove emojis
'''
def remove_emoji(text):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

'''
    Decontraction of the tweets
'''
def remove_emoji(text):
    text = re.sub(r"won\'t", " will not", text)
    text = re.sub(r"won\'t've", " will not have", text)
    text = re.sub(r"can\'t", " can not", text)
    text = re.sub(r"don\'t", " do not", text)
    text = re.sub(r"can\'t've", " can not have", text)
    text = re.sub(r"ma\'am", " madam", text)
    text = re.sub(r"let\'s", " let us", text)
    text = re.sub(r"ain\'t", " am not", text)
    text = re.sub(r"shan\'t", " shall not", text)
    text = re.sub(r"sha\n't", " shall not", text)
    text = re.sub(r"o\'clock", " of the clock", text)
    text = re.sub(r"y\'all", " you all", text)
    text = re.sub(r"n\'t", " not", text)
    text = re.sub(r"n\'t've", " not have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'s", " is", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'d've", " would have", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ll've", " will have", text)
    text = re.sub(r"\'t", " not", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'m", " am", text)
    text = re.sub(r"\'re", " are", text)
    return text  

'''
   Seperate alphanumberic textual data
'''
def seperate_alpha_num(text):
    temp = text
    words = re.findall(r"[^\W\d_]+|\d+", temp)
    return " ".join(words)

'''
    Count repeating characters
'''
def cont_rep_char(text):
    tchr = text.group(0) 
    if len(tchr) > 1:
        return tchr[0:2]

'''
    Unique characters
'''

def unique_char(rep, text):
    substitute = re.sub(r'(\w)\1+', rep, text)
    return substitute

'''
    substitute character
'''

def char(text):
    substitute = re.sub(r'[^a-zA-Z]',' ',text)
    return substitute

'''
    Load data
'''
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

positive = df[df['airline_sentiment'] == 'positive'].text
neutral = df[df['airline_sentiment'] == 'neutral'].text
negative = df[df['airline_sentiment'] == 'negative'].text

df.airline_sentiment = df.airline_sentiment.apply(lambda x : convert_Sentiment(x))
print(df.airline_sentiment)


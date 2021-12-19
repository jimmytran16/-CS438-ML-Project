# Basic Operation
import pandas as pd
import numpy as np

# Text Preprocessing & Cleaning
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import re

from sklearn.model_selection import learning_curve

from sklearn.model_selection import train_test_split # Split Data 
from imblearn.over_sampling import SMOTE # Handling Imbalanced

# Model Building
from sklearn.model_selection import GridSearchCV
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC


from sklearn.metrics import classification_report , confusion_matrix , accuracy_score # Performance Metrics  
from sklearn.metrics import roc_curve, auc

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
def remove_url(tweetData):
    url = re.compile(r'https?://\S+|www\.\S+')
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
def decontraction(text):
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
def seperate_alphanumeric(text):
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


# combaine negative reason with  tweet (if exsist)
df['final_text'] = df['negativereason'].fillna('') + ' ' + df['text'] 


# Apply functions on tweets
df['final_text'] = df['final_text'].apply(lambda x : remove_username(x))
df['final_text'] = df['final_text'].apply(lambda x : remove_url(x))
df['final_text'] = df['final_text'].apply(lambda x : remove_emoji(x))
df['final_text'] = df['final_text'].apply(lambda x : decontraction(x))
df['final_text'] = df['final_text'].apply(lambda x : seperate_alphanumeric(x))
df['final_text'] = df['final_text'].apply(lambda x : unique_char(cont_rep_char,x))
df['final_text'] = df['final_text'].apply(lambda x : char(x))
df['final_text'] = df['final_text'].apply(lambda x : x.lower())
df['final_text'] = df['final_text'].apply(lambda x : remove_stopwords(x))

X = df['final_text']
y = df['airline_sentiment']

n_classes = 3

# Apply TFIDF on cleaned tweets
tfid = TfidfVectorizer()
X_final =  tfid.fit_transform(X)

smote = SMOTE()
x_sm,y_sm = smote.fit_resample(X_final,y)

# Split Data into train & test 
X_train , X_test , y_train , y_test = train_test_split(x_sm , y_sm , test_size=0.2)
X_train , X_val , y_train , y_val = train_test_split(X_train , y_train , test_size=0.25)

def plot_learning_curve(
    estimator,
    title,
    X,
    y,
    axes=None,
    ylim=None,
    cv=None,
    n_jobs=None,
    train_sizes=np.linspace(0.1, 1.0, 5),
):
    """
    Generate 3 plots: the test and training learning curve, the training
    samples vs fit times curve, the fit times vs score curve.

    Parameters
    ----------
    estimator : estimator instance
        An estimator instance implementing `fit` and `predict` methods which
        will be cloned for each validation.

    title : str
        Title for the chart.

    X : array-like of shape (n_samples, n_features)
        Training vector, where ``n_samples`` is the number of samples and
        ``n_features`` is the number of features.

    y : array-like of shape (n_samples) or (n_samples, n_features)
        Target relative to ``X`` for classification or regression;
        None for unsupervised learning.

    axes : array-like of shape (3,), default=None
        Axes to use for plotting the curves.

    ylim : tuple of shape (2,), default=None
        Defines minimum and maximum y-values plotted, e.g. (ymin, ymax).

    cv : int, cross-validation generator or an iterable, default=None
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:

          - None, to use the default 5-fold cross-validation,
          - integer, to specify the number of folds.
          - :term:`CV splitter`,
          - An iterable yielding (train, test) splits as arrays of indices.

        For integer/None inputs, if ``y`` is binary or multiclass,
        :class:`StratifiedKFold` used. If the estimator is not a classifier
        or if ``y`` is neither binary nor multiclass, :class:`KFold` is used.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validators that can be used here.

    n_jobs : int or None, default=None
        Number of jobs to run in parallel.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    train_sizes : array-like of shape (n_ticks,)
        Relative or absolute numbers of training examples that will be used to
        generate the learning curve. If the ``dtype`` is float, it is regarded
        as a fraction of the maximum size of the training set (that is
        determined by the selected validation method), i.e. it has to be within
        (0, 1]. Otherwise it is interpreted as absolute sizes of the training
        sets. Note that for classification the number of samples usually have
        to be big enough to contain at least one sample from each class.
        (default: np.linspace(0.1, 1.0, 5))
    """
    if axes is None:
        _, axes = plt.subplots(1, 3, figsize=(20, 5))

    axes[0].set_title(title)
    if ylim is not None:
        axes[0].set_ylim(*ylim)
    axes[0].set_xlabel("Training examples")
    axes[0].set_ylabel("Score")

    train_sizes, train_scores, test_scores, fit_times, _ = learning_curve(
        estimator,
        X,
        y,
        cv=cv,
        n_jobs=n_jobs,
        train_sizes=train_sizes,
        return_times=True,
    )
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    fit_times_mean = np.mean(fit_times, axis=1)
    fit_times_std = np.std(fit_times, axis=1)

    # Plot learning curve
    axes[0].grid()
    axes[0].fill_between(
        train_sizes,
        train_scores_mean - train_scores_std,
        train_scores_mean + train_scores_std,
        alpha=0.1,
        color="r",
    )
    axes[0].fill_between(
        train_sizes,
        test_scores_mean - test_scores_std,
        test_scores_mean + test_scores_std,
        alpha=0.1,
        color="g",
    )
    axes[0].plot(
        train_sizes, train_scores_mean, "o-", color="r", label="Training score"
    )
    axes[0].plot(
        train_sizes, test_scores_mean, "o-", color="g", label="Cross-validation score"
    )
    axes[0].legend(loc="best")

    # Plot n_samples vs fit_times
    axes[1].grid()
    axes[1].plot(train_sizes, fit_times_mean, "o-")
    axes[1].fill_between(
        train_sizes,
        fit_times_mean - fit_times_std,
        fit_times_mean + fit_times_std,
        alpha=0.1,
    )
    axes[1].set_xlabel("Training examples")
    axes[1].set_ylabel("fit_times")
    axes[1].set_title("Scalability of the model")

    # Plot fit_time vs score
    axes[2].grid()
    axes[2].plot(fit_times_mean, test_scores_mean, "o-")
    axes[2].fill_between(
        fit_times_mean,
        test_scores_mean - test_scores_std,
        test_scores_mean + test_scores_std,
        alpha=0.1,
    )
    axes[2].set_xlabel("fit_times")
    axes[2].set_ylabel("Score")
    axes[2].set_title("Performance of the model")

    return plt

title = r"Learning Curves (Logistic Regression)"
fig, axes = plt.subplots(3, 2, figsize=(10, 15))
plot_learning_curve(LogisticRegression(penalty = 'l2', C = 500,random_state = 0),title, x_sm, y_sm, axes=axes[:, 1], ylim=(0.7, 1.01), cv=5, n_jobs=4)
plt.show()

'''
    Logistic Regression
'''
LR = LogisticRegression(penalty = 'l2', C = 500,random_state = 0)
LR.fit(X_train,y_train)
LR_prediction =  LR.predict(X_val)
print(accuracy_score(LR_prediction,y_val))

'''
   Visualize model performance
'''
cr = classification_report(y_val, LR_prediction)
print("Classification Report Logistic Regression:\n----------------------\n", cr)
cm = confusion_matrix(y_test,LR_prediction)

'''
   Plot confusion matrix
'''
plt.figure(figsize=(8,6))
sentiment_classes = ['Negative', 'Neutral', 'Positive']
sns.heatmap(cm, cmap=plt.cm.Blues, annot=True, fmt='d', 
            xticklabels=sentiment_classes,
            yticklabels=sentiment_classes)
plt.title('Confusion matrix', fontsize=16)
plt.xlabel('Actual label', fontsize=12)
plt.ylabel('Predicted label', fontsize=12)
plt.show()

######################################################### SVM #########################################################



##param_grid = {'C': [10, 100], 'gamma': [1,0.1,0.01],'kernel': ['rbf', 'poly', 'sigmoid']}
##grid = GridSearchCV(SVC(),param_grid,refit=True,verbose=2)
##grid.fit(X_train,y_train)
##print(grid.best_estimator_)

title = r"Learning Curves (Support Vector Machines)"
fig, axes = plt.subplots(3, 2, figsize=(10, 15))
plot_learning_curve(SVC(C=100,gamma=1),title, x_sm, y_sm, axes=axes[:, 1], ylim=(0.7, 1.01), cv=5, n_jobs=4)
plt.show()

svm = SVC(C=100,gamma=1)
svm.fit(X_train,y_train)
svm_prediction =  svm.predict(X_val)
print(accuracy_score(svm_prediction,y_val))

'''
   Visualize model performance
'''
cr = classification_report(y_val, svm_prediction)
print("Classification Report SVM:\n----------------------\n", cr)
cm = confusion_matrix(y_test,svm_prediction)


'''
   Plot confusion matrix
'''
plt.figure(figsize=(8,6))
sentiment_classes = ['Negative', 'Neutral', 'Positive']
sns.heatmap(cm, cmap=plt.cm.Blues, annot=True, fmt='d', 
            xticklabels=sentiment_classes,
            yticklabels=sentiment_classes)
plt.title('Confusion matrix', fontsize=16)
plt.xlabel('Actual label', fontsize=12)
plt.ylabel('Predicted label', fontsize=12)
plt.show()



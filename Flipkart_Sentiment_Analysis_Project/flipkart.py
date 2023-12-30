"""
GeeksForGeeks: Flipkart Reviews Sentiment Analysis using Python
Using code from: https://www.geeksforgeeks.org/flipkart-reviews-sentiment-analysis-using-python/?ref=lbp
"""

# Import necessary libraries for EDA (Exploratory Data Analysis)
"""
Pandas : For importing the dataset
Scikit-learn : For importing the model, accuracy module, 
    and TfidfVectorizer (TF-IDF stands for Term Frequency Inverse Document Frequency of records. 
    It can be defined as the calculation of how relevant a word in a series or corpus is to a text)
Warning : To ignore all the warnings
Re: Libary used to clean data
Matplotlib : To plot the visualization
Seaborn : For data visualization
"""
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import re
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt

# Import NLTK library for (NLP) Natural Language Processing
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('punkt')

# Import data into data frame variable (df) and peek at first 5 rows
df = pd.read_csv('flipkart_data.csv')
df.head()

"""
Assume that customer sentiments are seen through ratings,
we section the ratings into 2 classes based on unique ratings
"""
pd.unique(df['rating'])

# Creates countplot to visualize the ratings data
sns.countplot(data = df, x = 'rating', order = df.rating.value_counts().index)

"""
Setting a check at ratings above or at 5 such that they are
deemed positive sentiments while those below are negative.
Positive - 1, Negative - 0
"""
pos_neg = []
for i in range(len(df['rating'])):
    if df['rating'][i] >= 5:
        pos_neg.append(1)
    else:
        pos_neg.append(0)
  
df['label'] = pos_neg

# TDQM library makes iterables show a smart progress meter
from tqdm import tqdm

"""
Creates a function that preprocesses the text as a way to filter out 
punctuation and leave key words/phrases that represent sentiments
"""
def preprocess_text(text_data):
    preprocessed_text = []
  
    for sentence in tqdm(text_data):
        # Removes punctuations
        sentence = re.sub(r'[^\w\s]', '', sentence)
  
        # Converts to lowercase and removes stopwords (common words like 'in', 'is', and 'an')
        preprocessed_text.append(' '.join(token.lower()
                                          for token in nltk.word_tokenize(sentence)
                                          if token.lower() not in stopwords.words('english')))
  
    return preprocessed_text

# Implement the function on the dataset of reviews
preprocessed_review = preprocess_text(df['review'].values)
df['review'] = preprocessed_review

df.head()

df["label"].value_counts()

"""
Start by creating vectors using TF-IDF which calculates 
how relevant a word in a series or corpus is to a text.
The meaning increases proportionally to the number of 
times in the text a word appears but is compensated 
by the word frequency in the corpus (data-set)
"""
cv = TfidfVectorizer(max_features=2500)
X = cv.fit_transform(df['review'] ).toarray()

#prints vector that was transformed to fit to an array
X

# Start by performing the train-test split to explore machine learning models to train the data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, df['label'], test_size=0.33, stratify = df['label'], random_state = 42)

"""
We can now train any model we need, so we look into Decision Trees.
- A decision tree is a flowchart-like tree structure where each 
    internal node denotes the feature, branches denote the rules and 
    the leaf nodes denote the result of the algorithm.
"""
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
  
model = DecisionTreeClassifier(random_state=0)
model.fit(X_train,y_train)
  
# Code for testing the model and seeing accuracy of dataset
pred = model.predict(X_train)
accuracy_score = metrics.accuracy_score(y_train,pred)
print("Accuracy:", accuracy_score)

"""
We create a confusion matrix to visualize the accuracy of the trained dataset.
A confusion matrix is a matrix that summarizes the performance 
of a machine learning model on a set of test data. 
It is often used to measure the performance of classification models, 
which aim to predict a categorical label for each input instance. 
The matrix displays the number of true positives (TP), true negatives (TN), 
false positives (FP), and false negatives (FN) produced by the model on the test data
"""
# using metrics sub module from earlier (from sklearn import metrics)
cm = metrics.confusion_matrix(y_train,pred)
  
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm, display_labels = [False, True])
  
cm_display.plot()
plt.show()
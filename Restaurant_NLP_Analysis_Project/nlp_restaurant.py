"""
GeeksForGeeks: Python | NLP analysis of Restaurant reviews
Using code from: https://www.geeksforgeeks.org/python-nlp-analysis-of-restaurant-reviews/
"""

# Import necessary libraries for EDA (Exploratory Data Analysis)
"""
Pandas : For importing the dataset
Re: Libary used to clean data
Scikit-Learn: For machine learning models and statistical modelling
Natural Language Toolkit Library - Used for Text Preprocessing like Tokenization etc.
Matplotlib : To plot the visualization
"""
import pandas as pd
import re
import nltk
import matplotlib.pyplot as plt
nltk.download('stopwords')
 
# to remove stopword
from nltk.corpus import stopwords
 
# for Stemming propose
from nltk.stem.porter import PorterStemmer

# Import data into data frame variable (df) and peek at first 5 rows
"""
Importing dataset with setting delimiter as ‘\t’ as columns are separated as tab space. 
First column is about reviews of people 
Second column has 0s for negative reviews and 1s for positive reviews
Reviews and their category(0 or 1) are not separated by any other symbol 
but with tab space as most of the other symbols are characters in the review.
This is done to prevent any strange behaviors like errors or unreadable outputs.
"""
df = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t')
df.head()

# Cleaning/Preprocessing text 
"""
Remove Punctuations, Numbers: Punctuations, 
    Numbers don’t help much in processing the given text, if included, 
    they will just increase the size of a bag of words that we will create 
    as the last step and decrease the efficiency of an algorithm.
Stemming: Take roots of the word 
Convert each word into its lower case: For example, it is useless to have 
    some words in different cases (eg ‘good’ and ‘GOOD’).
"""
# Initialize an empty array (corpus) to append clean text
corpus = []
 
# 1000 (reviews) rows to clean
for i in range(0, 1000):
     
    # Column : "Review", row ith
    review = re.sub('[^a-zA-Z]', ' ', df['Review'][i])
     
    # Convert all cases to lower cases
    review = review.lower()
     
    # Split to array (default delimiter is " ")
    review = review.split()
     
    # Creating PorterStemmer object to take main stem of each word
    ps = PorterStemmer()
     
    # Loop for stemming each word in string array at ith row   
    review = [ps.stem(word) for word in review
                if not word in set(stopwords.words('english'))]
                 
    # Use .join function to all string array elements to bring it back into a string
    review = ' '.join(review) 
     
    # Append each string to generate the array of clean text
    corpus.append(review)

# Remove comment to view the corpus variable below
# corpus

# Tokenizing involves splitting sentences and words from the body of the text

"""
Making the bag of words via sparse matrix 
    Take all the different words of reviews in the dataset without repeating of words.
    One column for each word, therefore there is going to be many columns.
    Rows are reviews
    If a word is there in the row of a dataset of reviews, 
    then the count of the word will be there in the row of 
    a bag of words under the column of the word.

We use the CountVectorizer class from sklearn.feature_extraction.text. 
    Set a max number of features (max no. features which help the most via attribute “max_features”). 
    Do the training on the corpus and then apply the same transformation to the corpus “.fit_transform(corpus)” 
        and then convert it into an array. 
    If the review is positive or negative that answer is in the second column of the dataset[:, 1]: 
        all rows and 1st column (indexing from zero)
"""

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
 
# To extract max 1500 feature.
# "max_features" attribute can be changed for better results
cv = CountVectorizer(max_features = 1500)
 
# X contains corpus (dependent variable)
X = cv.fit_transform(corpus).toarray()
 
# y contains answers if review is positive or negative
y = df.iloc[:, 1].values

"""
Random forest is a Supervised Machine Learning Algorithm that 
    is used widely in Classification and Regression problems. 
It builds decision trees on different samples and takes their 
    majority vote for classification and average in case of regression.

Random forest is a versatile machine learning algorithm 
    developed by Leo Breiman and Adele Cutler that leverages an ensemble 
    of multiple decision trees to generate predictions or classifications. 
By combining the outputs of these trees, the random forest algorithm 
    delivers a consolidated and more accurate result
"""

# Splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
 
# Experimenting with "test_size" to get desired results
"""
Split can be made 70/30 or 80/20 or 85/15 or 75/25,  
X is the bag of words model, y is 0 or 1 (positive or negative)
"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15)


# Fitting Random Forest Classification to training set
from sklearn.ensemble import RandomForestClassifier
# Adding sublibrary metrics for accuracy testing
from sklearn import metrics

# The n_estimators parameter can be seen as number of trees 
# We can modify n_estimators to get desired results
model = RandomForestClassifier(n_estimators = 501, criterion = 'entropy')
                             
model.fit(X_train, y_train)

# Code for testing the model and seeing accuracy of training dataset
y_train_pred = model.predict(X_train)

#y_train_pred

print("Training dataset accuracy score: ", metrics.accuracy_score(y_train, y_train_pred))

# Code for testing the model and seeing accuracy of test dataset
y_test_pred = model.predict(X_test)

#y_test_pred

print("Test dataset accuracy score: ", metrics.accuracy_score(y_test, y_test_pred))

"""
Creating confusion matrix for dataset
TRUE POSITIVE : measures the proportion of actual positives 
    that are correctly identified. 
TRUE NEGATIVE : measures the proportion of actual positives 
    that are not correctly identified. 
FALSE POSITIVE : measures the proportion of actual negatives 
    that are correctly identified. 
FALSE NEGATIVE : measures the proportion of actual negatives 
    that are not correctly identified.
"""

# Using metrics sub module from earlier (from sklearn import metrics)
# For training dataset
cm_train = metrics.confusion_matrix(y_train, y_train_pred)

# cm_train
  
cm_train_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm_train, display_labels = [False, True])

print("\nTraining dataset Confusion Matrix: ") 
cm_train_display.plot()
plt.show()

# For test dataset
cm_test = metrics.confusion_matrix(y_test, y_test_pred)

# cm_train
  
cm_test_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm_test, display_labels = [False, True])

print("\nTest dataset Confusion Matrix: ")
cm_test_display.plot()
plt.show()


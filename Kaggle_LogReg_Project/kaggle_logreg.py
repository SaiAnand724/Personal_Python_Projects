"""
GeeksForGeeks: ML | Kaggle Breast Cancer Wisconsin Diagnosis using Logistic Regression
Using code from: https://www.geeksforgeeks.org/ml-kaggle-breast-cancer-wisconsin-diagnosis-using-logistic-regression/?ref=lbp
"""

# Import necessary libraries for EDA (Exploratory Data Analysis)
"""
NumPy: For computational power of data
Pandas : For importing the dataset and processing
Scikit-Learn: For machine learning models and statistical modelling
Matplotlib : To plot the visualization
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing data into dataframe object
df = pd.read_csv("breastcancerdataset.csv")

# Peeks at the first 5 rows of raw dataset
df.head()

# Check dataset for irrelevant columns to begin cleaning process
df.info()

# Dropping the Unamed 32 and id columns as they are uneeded for predictive analysis
df = df.drop(['Unnamed: 32', 'id'], axis = 1)

"""
Converting the diagnosis column into numerical values such that:
M = Malignant or B = Benign => M = 1 , B = 0
"""
df.diagnosis = [1 if each == "M" else 0 for each in df.diagnosis]

# Peeks at first 5 rows of filtered dataset
df.head()

"""
Separated data into objects "x_data" and "y" such that
x_data stores the data for the other columns other than diagnosis
y stores the values for the diagnosis column
"""
y = df.diagnosis.values
x_data = df.drop(['diagnosis'], axis = 1)

"""
Normalization is usually done the practice of organizing data entries to 
    ensure they appear similar across all fields and records, making 
    information easier to find, group and analyze
Normalize data values in "x_data" object and store in "x" object
"""
x = ((x_data - np.min(x_data))/(np.max(x_data) - np.min(x_data))).values


"""
Imported the train_test_split function from sklearn submodule model_selection
to split our original dataframe (after normalization step above), with a ratio
"""
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.15, random_state = 42)

# Performed the transpose function on each set
"""
Transpose: The transpose of a matrix is the process of interchanging 
    the row of a matrix with the column and vice-versa.
"""
x_train = x_train.T
x_test = x_test.T
y_train = y_train.T
y_test = y_test.T
 
# Print the shape of each set
print("x train set shape: ", x_train.shape)
print("x test set shape: ", x_test.shape)
print("y train set shape: ", y_train.shape)
print("y test set shape: ", y_test.shape)

# Create a function that initializes default values for weights and bias
def initialize_weights_and_bias(dimension):
    w = np.full((dimension, 1), 0.01)
    b = 0.0
    return w, b

"""
Created sigmoid function for easier logistic regression computations
The sigmoid is a mathematical function that maps input values to a value between 0 and 1,
    such that it restricts the outcome value to lie in between 0 and 1 no matter 
    what the value of X is which makes it useful for 
    binary classification and logistic regression problems.
"""
def sigmoid(z):
    y_head = 1/(1 + np.exp(-z))
    return y_head

"""
Created forward/backward propogation function

Weights increase the steepness of activation function. 
    This means weight decide how fast the activation function will trigger 
    whereas bias is used to delay the triggering of the activation function.

For logistic regression, the forward propagation is used to calculate 
    the cost function and the output, y (y_head), while the 
    backward propagation is used to calculate the gradient descent
"""
def forward_backward_propagation(w, b, x_train, y_train):
    z = np.dot(w.T, x_train) + b
    y_head = sigmoid(z)
    loss = - y_train * np.log(y_head) - (1 - y_train) * np.log(1 - y_head)
    # x_train.shape[1] element is used for scaling purposes
    cost = (np.sum(loss)) / x_train.shape[1]     
 
    # backward propagation portion of the function
    derivative_weight = (np.dot(x_train, ((y_head - y_train).T))) / x_train.shape[1]
    derivative_bias = np.sum(y_head-y_train) / x_train.shape[1]                
    gradients = {"derivative_weight": derivative_weight, "derivative_bias": derivative_bias}
    
    return cost, gradients

"""
Created an update function that initializes the w (weight) and b (bias) with
    new values using forward and backward propogation with a certain amount of iterations
"""
def update(w, b, x_train, y_train, learning_rate, number_of_iterations):
    # Stores initial costs
    cost_list = []
    # Used to store costs and their index at certain intervals
    cost_list2 = []
    index = []
 
    # Update learning parameters by number_of_iterations 
    for i in range(number_of_iterations):
        # Use forward and backward propagation to find cost and gradient values
        cost, gradients = forward_backward_propagation(w, b, x_train, y_train)
        cost_list.append(cost)
 
        # Update weight and bias values using learning_rate value
        w = w - learning_rate * gradients["derivative_weight"]
        b = b - learning_rate * gradients["derivative_bias"]
        if i % 10 == 0:
            cost_list2.append(cost)
            index.append(i)
            print ("Cost after iteration % i: % f" %(i, cost))
 
    # Update learning parameters (weights and bias)
    parameters = {"weight": w, "bias": b}
    plt.plot(index, cost_list2)
    plt.xticks(index, rotation ='vertical')
    plt.xlabel("Number of Iterations")
    plt.ylabel("Cost")
    plt.show()
    return parameters, gradients, cost_list

"""
Create a predict function that outputs the behaviors of the predicted
data based on learned weights and biases
"""
def predict(w, b, x_test):
    # x_test is an input for forward propagation
    z = sigmoid(np.dot(w.T, x_test) + b)
    # Y_prediction is an array filled with zeros 
    # x_train.shape[1] element is used for scaling purposes
    Y_prediction = np.zeros((1, x_test.shape[1]))
 
    # Z value predicts the behavior of y_head, sigmoid curve
    for i in range(z.shape[1]):
        # if z <= 0.5, prediction is sign zero (y_head = 0)
        if z[0, i]<= 0.5:
            Y_prediction[0, i] = 0
        # if z > 0.5, prediction is sign one (y_head = 1)
        else:
            Y_prediction[0, i] = 1
    
    print("Y_prediction values: ", Y_prediction)
 
    return Y_prediction



"""
Create logistic regression function through a culmination of efforts
from above functions
"""
def logistic_regression(x_train, y_train, x_test, y_test, learning_rate, num_iterations):
 
    dimension = x_train.shape[0]
    w, b = initialize_weights_and_bias(dimension)
    
    # Update parameters with update() function
    parameters, gradients, cost_list = update(w, b, x_train, y_train, learning_rate, num_iterations)
    
    # Training set prediction
    y_prediction_train = predict(parameters["weight"], parameters["bias"], x_train)
    
    # Test set predictions
    y_prediction_test = predict(parameters["weight"], parameters["bias"], x_test)
    
 
    # Train and test dataset accuracy score
    print("Train accuracy: {} %".format(100 - np.mean(np.abs(y_prediction_train - y_train)) * 100))
    print("Test accuracy: {} %".format(100 - np.mean(np.abs(y_prediction_test - y_test)) * 100))
     
# Logistic regression method call
logistic_regression(x_train, y_train, x_test, y_test, learning_rate = 1, num_iterations = 150)
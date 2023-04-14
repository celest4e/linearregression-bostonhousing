import numpy as np
from matplotlib import pyplot as plt
from math import sqrt

# import data from csv file
data = np.genfromtxt('data/bostonhousing.csv', dtype=float, delimiter=',', names=True)

# establish RM and MEDV as independent and dependent variables
x_values = data['RM']
y_values = data['MEDV']

# find slopes and intercept to 
slope = find_slope(x_values, y_values)
intercept = find_intercept(x_values, y_values)

# find predicted y values
predicted_y_values = slope * x_values + intercept

# plot scatterplot of original points
plt.scatter(x_values, y_values, color='g')

# plot linear regression model
plt.plot(x_values, predicted_y_values, '-r', label='linear regression fit')

# graph details, and display
plt.title('Simple Linear Regression Fit of RM vs MEDV from the Boston Housing Dataset')
plt.xlabel('RM', color='#1C2833')
plt.ylabel('MEDV', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()

# Finds the y-intercept given list of x-values and list of y-values
# Parameter: x_values, a list; y_values, a list
# Precondition: x_values and y_values are lists of solely numeric values
# Return: returns the y-intercept value
# Postcondition: Returned value must be a numeric value
def find_intercept(x_values, y_values):
    return find_mean(y_values) - find_mean(x_values) * find_slope(x_values, y_values)

# Finds the slope given list of x-values and list of y-values
# Parameter: x_values, a list; y_values, a list
# Precondition: x_values and y_values are lists of solely numeric values
# Return: returns the slope value
# Postcondition: Returned value must be a numeric value
def find_slope(x_values, y_values):
    return find_r(x_values, y_values) * find_stdev(y_values) / find_stdev(x_values)

# Finds the standard deviation in a list of numbers
# Parameter: values, a list
# Precondition: values is a list of solely numeric values
# Return: returns the average of all of the numbers in values
# Postcondition: Returned value must be a numeric value
def find_stdev(values):
    vals = values - find_mean(values)
    vals = vals ** 2
    s = np.sum(vals)
    return sqrt(s / (len(values) - 1))

# Finds the correlation coefficient r given list of x-values and list of y-values
# Parameter: x_values, a list; y_values, a list
# Precondition: x_values and y_values are lists of solely numeric values
# Return: returns the correlation coefficient value
# Postcondition: Returned value must be a numeric value
def find_r(x_values, y_values):
    x_vals = x_values - find_mean(x_values)
    y_vals = y_values - find_mean(y_values)
    numerator = np.sum(x_vals * y_vals)
    denominator_x = np.sum(x_vals ** 2)
    denominator_y = np.sum(y_vals ** 2)
    return numerator / sqrt(denominator_x * denominator_y)

# Finds the mean in a list of numbers
# Parameter: values, a list
# Precondition: values is a list of solely numeric values
# Return: returns the average of all of the numbers in values
# Postcondition: Returned value must be a numeric value
def find_mean(values):
    return np.sum(values) / len(values)



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
    mean = find_mean(values)
    s = 0
    for value in values:
        s += (value - mean) ** 2
    return sqrt(s / (len(values) - 1))

# Finds the correlation coefficient r given list of x-values and list of y-values
# Parameter: x_values, a list; y_values, a list
# Precondition: x_values and y_values are lists of solely numeric values
# Return: returns the correlation coefficient value
# Postcondition: Returned value must be a numeric value
def find_r(x_values, y_values):
    x_mean = find_mean(x_values)
    y_mean = find_mean(y_values)
    numerator = 0
    denominator_x = 0
    denominator_y = 0
    for i in range(len(x_values)):
        numerator += (x_values[i] - x_mean) * (y_values[i] - y_mean)
        denominator_x += (x_values[i] - x_mean) ** 2
        denominator_y += (y_values[i] - y_mean) ** 2
    return numerator / sqrt(denominator_x * denominator_y)

# Finds the mean in a list of numbers
# Parameter: values, a list
# Precondition: values is a list of solely numeric values
# Return: returns the average of all of the numbers in values
# Postcondition: Returned value must be a numeric value
def find_mean(values):
    sum = 0
    for value in values:
        sum += value
    return sum / len(values)
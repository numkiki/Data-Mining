# Import used Library for this Lab:
import numpy as np
import pandas as pd
import math

#Function used for this Lab:

# Dataset functions:
# 1/ Load Dataset:
def loadData(filename):
    house_df = pd.read_csv(filename)
    return house_df

# 2/ Get the number of instances in the dataset:
def numOfInstances(house_df):
    return house_df.shape[0]

# 3/ Get the number of attributes in the dataset:
def numOfAttributes(house_df):
    return house_df.shape[1]

# 4/ Checking value is NaN or not:
def checkNaN(value):
    return value != value

# 6/ Checking each of elements in the array whether they are NaN or not:
def checkNaNArray(array):
    arr = []
    for i in array:
        arr.append(checkNaN(i))
    return arr

# 7/ Checking whether that attribute is missing data:
def checkMissing(house_df):
    checkMiss = []
    attributes = list(house_df.keys())
    numInstance = numOfInstances(house_df)
    for i in attributes:
        for index in range(numInstance):
            if(checkNaN(house_df[i][index])):
                checkMiss.append(i)
                break
    return checkMiss

# 8/ 
def listNumOfMissing(house_df):
    NumberOfMissing = {}  # constaint attribute and number of missing data
    attributes = list(house_df.keys())    
    NumOfInstances = numOfInstances(house_df)  # get the number of Instances
    for i in attributes:  # Check each of attributes
        MissingArray = checkNaNArray(house_df[i])  # IsNaN = 1      NotIsNaN = 0
        NumOfMiss = 0
        for index in range(NumOfInstances):
            NumOfMiss += int(MissingArray[index])
        NumberOfMissing[i] = NumOfMiss
    return NumberOfMissing

# 9/ Counting total missing value rows:
#Method 1:
def countMissingRows(house_df):
    missValue = house_df.isna().any(axis=1).sum()
    return missValue
#Method 2: prefer this method
def Test_CountingMissRows(house_df):
    attributes = list(house_df.keys())    
    for i in attributes:
        MissingArray = checkNaNArray(house_df[i])
    return MissingArray.count(False)

# Calculate Mean function:
def means(array):
    sum_score = 0
    count = 0
    for i in range(array.shape[0]):
        if (checkNaN(array[i]) == False):
            sum_score += array[i]
            count += 1
    return round((sum_score / count), 2)

# Calculate Median function:
def median(array):
    score = []
    for i in range(array.shape[0]):
        if (checkNaN(array[i]) == False):
            score.append(array[i])
    sorted_score = score.sort()
    n = int(len(sorted_score) / 2)
    if (n % 2 == 0):
        return (sorted_score[n - 1] + sorted_score[n]) / 2
    else:
        return sorted_score[n]
    
#Calculate Mode function:
def mode(array):
    score = {}
    for i in range(array.shape[0]):
        if (checkNaN(array[i]) == False):
            if array[i] not in score:
                score[array[i]] = 1
            else:
                score[array[i]] += 1
    max = 0
    result = 0
    for val in score:
        if (max < score[val]):
            max = score[val]
            result = val
    return result










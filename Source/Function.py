import pandas as pd
import numpy as np
import math 
import csv

# Load Dataset:
def loadData(filename):
    house_df = pd.read_csv(filename)
    return house_df

# Get the number of instances in the dataset:
def numOfInstances(house_df):
    return house_df.shape[0]

# Get the number of attributes in the dataset:
def numOfAttributes(house_df):
    return house_df.shape[1]

# Checking value is NaN or not:
def checkNaN(value):
    return value != value

# Checking each of elements in the array whether they are NaN or not:
def checkNaNArray(array):
    arr = []
    for i in array:
        arr.append(checkNaN(i)) #return a list of Trues and Falses
    return arr

# Checking whether that attribute is missing data:
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
# 
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

# Counting total rows that have any missing value:
def countMissingRows(house_df):
    missvalue = 0
    for i in range(len(house_df)):
        if True in checkNaNArray(list(house_df.loc[i])):
            missvalue+=1
    return missvalue

# Calculate Mean:
def average(single_array):
    sum = 0
    count = 0
    for i in single_array:
        if checkNaN(i) == False:
            sum += i
            count+=1
    if (sum == 0 and count == 0):
        return 0
    return round(sum/count, 2)

def fillMean(column, dataset, output):
    subDataset = dataset[column]
    numCols = len(column)
    key_value = {}

    for i in column: # go through each column
        imputeValue = average(subDataset[i])
        for j in range(len(subDataset[i])):  # go through each row      
            if checkNaN(subDataset.loc[j, i]):
                subDataset.loc[j, i] = imputeValue
        key_value[i] = subDataset[i]        
    
    df = pd.DataFrame(key_value)
    df.to_csv(output, index=False)
    return output
# Calculate Median:
def median(col): 
    nan_filter = []
    for i in col:
        if (checkNaN(i) == False):
            nan_filter.append(i)
    sorted_filter = sorted(nan_filter)
    n = int(len(sorted_filter) / 2)
    if (n % 2 != 0):
        return (sorted_filter[n - 1] + sorted_filter[n]) / 2
    else:
        return sorted_filter[n]
        
def fillMedian(column, dataset, output): # for quantitative attributes
    subDataset = dataset[column]
    numCols = len(column)
    key_value = {}

    for i in column: # go through each column
        imputeValue = median(subDataset[i])
        for j in range(len(subDataset[i])):  # go through each row      
            if checkNaN(subDataset.loc[j, i]):
                subDataset.loc[j, i] = imputeValue
        key_value[i] = subDataset[i]        
    
    df = pd.DataFrame(key_value)
    df.to_csv(output, index=False)
    return output
# Calculate Mode 
def mode (col):
    freq = {}
    for i in col:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    freq_val = max(freq.values())
    modes = [key for key, value in freq.items() if value == freq_val]
    return modes

def fillMode(column, dataset, output):
    subDataset = dataset[column]
    numCols = len(column)
    key_value = {}

    for i in column: # go through each column
        imputeValue = mode(subDataset[i])[0]
        for j in range(len(subDataset[i])):  # go through each row      
            if checkNaN(subDataset.loc[j, i]):
                subDataset.loc[j, i] = imputeValue
        key_value[i] = subDataset[i]     

    df = pd.DataFrame(key_value)
    df.to_csv(output, index=False)
    return output

#Delete the row with missing value:
def deleteRowMissing(dataset,missing_rate,output):
    numInstances = numOfInstances(dataset)
    numAttributes = numOfAttributes(dataset)
    for row in dataset:
        if (numAttributes == 0):
            numAttributes = len(row)
            continue  
        NumOfMissing = 0
        for i in row:
            if (checkNaN(i)):
                NumOfMissing += 1
        if (NumOfMissing > missing_rate * numAttributes):
            del dataset[row]
    dataset.to_csv(output)
    print("Instances before deleting:", numInstances)
    print("Instances left after deleting the missing value rows with missing rate more than", missing_rate,":", len(dataset))

#Delete the column with missing value:
def deleteColMissing(dataset,missing_rate,output):
    numAttributes = numOfAttributes(dataset)
    numMissing = listNumOfMissing(dataset)
    attributes = list(dataset.keys())

    for attribute in attributes:
        if (numMissing[attribute] > (missing_rate * numAttributes)):
            del dataset[attribute]
    dataset.to_csv(output)
    print("Attributes before deleting:", numAttributes)
    print("Attributes left after deleting the missing value columns with missing rate more than", missing_rate,":", len(dataset.keys()))

# Remove duplicates
def removeDuplicates(dataset):
    tempList = dataset.values.tolist()
    separator = ', '
    joinedList = [separator.join(map(str, innerList)) for innerList in tempList]

    unique_row = []
    output_csv_row = []

    for i in range(len(joinedList)):
        if joinedList[i] not in unique_row:
            unique_row.append(joinedList[i])
            output_csv_row.append(tempList[i])

    df = pd.DataFrame(output_csv_row, columns=dataset.columns)
    df.to_csv("output_remove_dup.csv", index=False)
    return len(unique_row), df

def getNumericAttr(dataset):
    columns = dataset.dtypes
    res = []
    for i in (dataset.columns):
        if (columns[i] in [np.int64, np.float64]):
            res.append(i)
    return res

# Min-Max normalization
def minmax_normalization(dataset, newMax, newMin, column):
    columns = getNumericAttr(dataset)

    imputed_dataset = fillMean(columns, dataset, "imputed_mean.csv")
    temp_csv = loadData(imputed_dataset)
    final_dataset = removeDuplicates(temp_csv)[1]

    min_max = {}
    attributes = final_dataset.columns.tolist()
    if (column in attributes):
        length = len(final_dataset)
        maxData = final_dataset[column][0]
        minData = final_dataset[column][0]
        for i in range(length):
            if(final_dataset[column][i] > maxData):
                maxData = float(final_dataset[column][i])
            elif(final_dataset[column][i] < minData):
                minData = float(final_dataset[column][i])
        tempData = []
        for i in range(0, length):
            value = round(((final_dataset[column][i]-minData)/(maxData-minData) * (newMax-newMin)) + newMin, 2)
            tempData.append(value)
        min_max[column] = tempData
        df = pd.DataFrame(min_max)
        df.to_csv("minmax_norm.csv", index=False)
    else:
        print("Wrong attribute type")   

def StandardDeviation(col):
    mean = average(col)
    sqr_gap = 0
    
    for i in range(0, len(col)):
        sqr_gap += pow(abs(col[i] - mean), 2)
    variance = sqr_gap/len(col)  
    sd = math.sqrt(variance)
    
    return sd

def zscore_normalization(dataset, column):
    columns = getNumericAttr(dataset)

    imputed_dataset = fillMean(columns, dataset, "imputed_mean.csv")
    temp_csv = loadData(imputed_dataset)
    final_dataset = removeDuplicates(temp_csv)[1]
    z_score = {}
    attributes = final_dataset.columns.tolist()
    if (column in attributes):
        mean = average(final_dataset[column])
        sd = StandardDeviation(final_dataset[column])
        tempData = []
        for i in range(0, len(final_dataset)):
            value = round((final_dataset[column][i]-mean)/sd, 2)
            tempData.append(value)
        z_score[column] = tempData
        df = pd.DataFrame(z_score)
        df.to_csv("zscore_norm.csv", index=False)
    else:
        print("Wrong attribute type")
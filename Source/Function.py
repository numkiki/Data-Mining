import pandas as pd
import numpy as np
import math 

# Load Dataset:
def loadData(filename):
    dataset = pd.read_csv(filename)
    return dataset

# Get the number of instances in the dataset:
def numOfInstances(dataset):
    return dataset.shape[0]

# Get the number of attributes in the dataset:
def numOfAttributes(dataset):
    return dataset.shape[1]

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
def checkMissing(dataset):
    checkMiss = []
    attributes = list(dataset.keys())
    numInstance = numOfInstances(dataset)
    for i in attributes:
        for j in range(numInstance):
            if(checkNaN(dataset[i][j])):
                checkMiss.append(i)
                break
    return checkMiss

# Counting the number of missing data
def numOfMissing(dataset):
    numMissing = {}
    attributes = list(dataset.keys())    
    NumOfInstances = numOfInstances(dataset)
    for i in attributes:  # Check each of attributes
        MissingArray = checkNaNArray(dataset[i])
        NumOfMiss = 0
        for j in range(NumOfInstances):
            NumOfMiss += int(MissingArray[j])
        numMissing[i] = NumOfMiss
    return numMissing

# Counting total rows that have any missing value:
def countMissingRows(house_df):
    missValue = 0
    for i in range(len(house_df)):
        if True in checkNaNArray(list(house_df.loc[i])):
            missValue += 1
    return missValue

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
        if checkNaN(i) == False:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
    print(freq)
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
        numMissing = 0
        for i in row:
            if (checkNaN(i)):
                numMissing += 1
        if (numMissing > (missing_rate * numAttributes)):
            del dataset[row]
    dataset.to_csv(output)
    print("Instances before deleting:", numInstances)
    print("Instances left after deleting the missing value rows with missing rate more than", missing_rate,":", len(dataset))

#Delete the column with missing value:
def deleteColMissing(dataset,missing_rate,output):
    numAttributes = numOfAttributes(dataset)
    numMissing = numOfMissing(dataset)
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
 
    attributes = final_dataset.columns.tolist()
    if (column in attributes):
        min_max = {}
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
        return True
    else:   
        return False

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
    
    attributes = final_dataset.columns.tolist()
    if (column in attributes):
        z_score = {}
        mean = average(final_dataset[column])
        sd = StandardDeviation(final_dataset[column])
        tempData = []
        for i in range(0, len(final_dataset)):
            value = round((final_dataset[column][i]-mean)/sd, 2)
            tempData.append(value)
        z_score[column] = tempData
        df = pd.DataFrame(z_score)
        df.to_csv("zscore_norm.csv", index=False)
        return True
    else:
        return False

def addition(dataset, col1, col2):
    columns = getNumericAttr(dataset) # get the numeric attributes

    imputed_dataset = fillMean(columns, dataset, "imputed_mean.csv") # fill the mean to nan
    temp_csv = loadData(imputed_dataset) # read the data after imputation
    final_dataset = removeDuplicates(temp_csv)[1] # final dataset after removing duplicates
    attributes = final_dataset.columns.tolist() # get the list of attributes
    addition_results = {}
    if (col1 in attributes and col2 in attributes):
        result = []
        for i in range(len(final_dataset)):
            add_value = final_dataset[col1][i] + final_dataset[col2][i]
            result.append(add_value)
        addition_results["AddedValue"] = result
        df = pd.DataFrame(addition_results)
        df.to_csv("add_2_columns.csv", index=False)
        return "A add_2_columns.csv has been created"
    else:
        return "Wrong attribute type"

def subtraction(dataset, col1, col2):
    columns = getNumericAttr(dataset) # get the numeric attributes

    imputed_dataset = fillMean(columns, dataset, "imputed_mean.csv") # fill the mean to nan
    temp_csv = loadData(imputed_dataset) # read the data after imputation
    final_dataset = removeDuplicates(temp_csv)[1] # final dataset after removing duplicates
    attributes = final_dataset.columns.tolist() # get the list of attributes
    subtraction_results = {}
    if (col1 in attributes and col2 in attributes):
        result = []
        for i in range(len(final_dataset)):
            sub_value = final_dataset[col1][i] - final_dataset[col2][i]
            result.append(sub_value)
        subtraction_results["SubtractedValue"] = result
        df = pd.DataFrame(subtraction_results)
        df.to_csv("subtract_2_columns.csv", index=False)
        return "A subtract_2_columns.csv has been created"
    else:
        return "Wrong attribute type"

def multiplication(dataset, col1, col2):
    columns = getNumericAttr(dataset) # get the numeric attributes

    imputed_dataset = fillMean(columns, dataset, "imputed_mean.csv") # fill the mean to nan
    temp_csv = loadData(imputed_dataset) # read the data after imputation
    final_dataset = removeDuplicates(temp_csv)[1] # final dataset after removing duplicates
    attributes = final_dataset.columns.tolist() # get the list of attributes
    multiplication_results = {}
    if (col1 in attributes and col2 in attributes):
        result = []
        for i in range(len(final_dataset)):
            multiply_value = final_dataset[col1][i] * final_dataset[col2][i]
            result.append(multiply_value)
        multiplication_results["MultipliedValue"] = result
        df = pd.DataFrame(multiplication_results)
        df.to_csv("multiply_2_columns.csv", index=False)
        return "A multiply_2_columns.csv has been created"
    else:
        return "Wrong attribute type"

def division(dataset, col1, col2):
    columns = getNumericAttr(dataset) # get the numeric attributes

    imputed_dataset = fillMean(columns, dataset, "imputed_mean.csv") # fill the mean to nan
    temp_csv = loadData(imputed_dataset) # read the data after imputation
    final_dataset = removeDuplicates(temp_csv)[1] # final dataset after removing duplicates
    attributes = final_dataset.columns.tolist() # get the list of attributes
    division_results = {}
    if (col1 in attributes and col2 in attributes):
        result = []
        for i in range(len(final_dataset)):
            if (final_dataset[col2][i] != 0):
                divide_value = float(final_dataset[col1][i]) / final_dataset[col2][i]
                result.append(divide_value)
            else: 
                result.append(0)
        division_results["DividedValue"] = result
        df = pd.DataFrame(division_results)
        df.to_csv("divide_2_columns.csv", index=False)
        return "A divide_2_columns.csv has been created"
    else:
        return "Wrong attribute type"
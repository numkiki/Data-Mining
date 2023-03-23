import pandas as pd

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
def fillMean(column, dataset, output):
    def average(single_array):
        sum = 0
        count = 0
        for i in single_array:
            if checkNaN(i) == False:
                sum += i
                count+=1
        return round(sum/count, 2)
    
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
    df.to_csv(output)
    print(len(key_value))

# Calculate Median:
def fillMedian(column, dataset, output): # for quantitative attributes
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
    print(len(key_value))
    df.to_csv(output)
# Calculate Mode 
def fillMode(column, dataset, output):
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

    subDataset = dataset[column]
    numCols = len(column)
    key_value = {}

    for i in column: # go through each column
        imputeValue = mode(subDataset[i])[0]
        for j in range(len(subDataset[i])):  # go through each row      
            if checkNaN(subDataset.loc[j, i]):
                subDataset.loc[j, i] = imputeValue
        key_value[i] = subDataset[i]     

    print(len(key_value))
    df = pd.DataFrame(key_value)
    df.to_csv(output)
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
    df.to_csv("output_remove_dup.csv")
    return len(unique_row)
    
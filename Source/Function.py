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
def mean(column, dataset):
    def average(single_array):
        sum = 0
        count = 0
        for i in single_array:
            if checkNaN(i) == False:
                sum += i
                count+=1
        return sum/count
    
    subDataset = dataset[column]
    numCols = len(column)
    print(numCols)
    # print(type(list(subDataset.values)))
    imputeValue = average(list(subDataset.values))
    print(imputeValue)
    for i in range(numCols):
        for j in subDataset.loc["LotArea"]:
            print(j)
        # print(subDataset.iloc[subDataset[i]])
        # imputeValue = average(subDataset.loc[i])
        # for j in range(len(subDataset.loc[i])):
        #     if checkNaN(subDataset.loc[i][j]) == True:
        #         subDataset.loc[i][j] = imputeValue

    # pd.to_csv(subDataset)

    # sum_score = 0
    # count = 0
    # if numCols <= 1:
    #     for i in range(numCols):
    #         if (checkNaN(array[i]) == False):
    #             sum_score += array[i]
    #             count += 1
    # else:
    #     for i in range(numCols):
    #         for j in range(numCols[0]):
                
    #     pass
    # avg = round((sum_score / count), 2)
    # return round((sum_score / count), 2)

# Calculate Median:
def median(array): # for quantitative attributes
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
    
#Calculate Mode for qualitative attributes:
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
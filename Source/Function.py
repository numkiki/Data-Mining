# Import used Library for this Lab:
import numpy as np
import pandas as pd
import math

#Function used for this Lab:

# Dataset functions:
# 1/ Load Dataset:
def loadData(filename):
    house_df = pd.read_csv("house-prices.csv")
    return house_df

# 2/ Get the number of instances in the dataset:
def numOfInstances(house_df):
    return house_df.shape[0]

# 3/ Get the number of attributes in the dataset:
def numOfAttributes(house_df):
    return house_df.shape[1]

# 





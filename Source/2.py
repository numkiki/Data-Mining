# Argument syntax: python 1.py input.csv
# Example:         python 1.py house-prices.csv

# Load the convenient packages
import sys
import Function
dataset = Function.loadData(sys.argv[1])

sum = Function.test(dataset)
print("Number of missing data rows: ",sum)
    
# Argument syntax: python 2.py input.csv
# Example:         python 2.py house-prices.csv

# Load the convenient packages
import sys
import Function
dataset = Function.loadData(sys.argv[1])

sum = Function.countMissingRows(dataset)
print(f"Number of rows with missing data: {sum}")
    
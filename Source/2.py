# Argument syntax: python 1.py input.csv
# Example:         python 1.py house-prices.csv

# Load the convenient packages
import sys
import Function
dataset = Function.loadData(sys.argv[1])

sum = Function.countMissingRows(dataset)
print(f"Number of rows with missing data: {sum}")
    
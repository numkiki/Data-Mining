# Requirement: Count the number of lines with missing data.
# Argument syntax: python 2.py -i input.csv
# Example:         python 2.py -i house-prices.csv

# Load the convenient packages
import argparse
import Function

parser = argparse.ArgumentParser(description=" ")

parser.add_argument('-i', '--input', required=True, help="input file: house-prices.csv")
args = parser.parse_args()

input = \
    args.input.lower()
dataset = Function.loadData(input)

sum = Function.countMissingRows(dataset)
print(f"Number of rows with missing data: {sum}")
    
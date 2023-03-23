# Argument syntax: python 1.py input.csv
# Example:         python 1.py house-prices.csv

# Load the convenient packages
import argparse
import Function

parser = argparse.ArgumentParser(description=" ")

parser.add_argument('-i', '--input', required=True, help="input file: house-prices.csv")
args = parser.parse_args()

input = \
    args.input.lower()
dataset = Function.loadData(input)
print("Attributes which have data missing:")
print(Function.checkMissing(dataset))
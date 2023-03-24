# Requirement: Deleting rows containing more than a particular number of missing values (Example: delete rows with the number of missing values is more than 50% of the number of attributes).
# Argument syntax: python 4.py -i input.csv -r missing_rate -o output.csv
# Example:         python 4.py -i house-prices.csv -r 50 -o output4.csv

import argparse
import Function

parser = argparse.ArgumentParser(description="Delete the row with missing data")

parser.add_argument('-i', '--input', required=True, help="input file: house-prices.csv")
parser.add_argument('-r', '--missing_rate', required=True, type = int, choices= range(50, 100),help= \
                    "Input a number >= 50")
parser.add_argument('-o', '--output', required=True, help="output file: output4.csv")

args = parser.parse_args()

input, missing_rate, output = \
    args.input.lower(), args.missing_rate ,args.output.lower()

dataset = Function.loadData(input)


if (missing_rate >= 50):
    missing_rate = missing_rate / 100
    Function.deleteRowMissing(dataset, missing_rate, output)
else:
    print("Cannot delete")
#  Deleting columns containing more than a particular number of missing values (Example: delete columns
#  with the number of missing values is more than 50% of the number of attributes).

# Argument syntax: python 5.py -i input.csv -r missing_rate -o output.csv
# Example: python 5.py -i house-prices.csv -r 50 -o new_output5.csv

import argparse
import Function

parser = argparse.ArgumentParser(description="Delete the column with missing data")

parser.add_argument('-i', '--input', required=True, help="input file: house-prices.csv")
parser.add_argument('-r', '--missing_rate', type = int, required=True ,help= \
                    "Input a number as an integer")
parser.add_argument('-o', '--output', required=True, help="output file: new_output5.csv")

args = parser.parse_args()

input, missing_rate, output = \
    args.input.lower(), args.missing_rate ,args.output.lower()

dataset = Function.loadData(input)
if (missing_rate >= 0 or missing_rate <= 100):
    missing_rate = missing_rate / 100
    Function.deleteColMissing(dataset, missing_rate, output)
else:
    print("Cannot delete")

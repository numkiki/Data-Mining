# Requirement: Fill in the missing value using mean, median (for numeric properties) and mode (for the categorical attribute).
# Argument syntax: python 3.py -i input.csv -m method -c column -o output.csv
# Example:         python 3.py -i house-prices.csv -m mean -c LotArea Id -o output_mean.csv

# Load the convenient packages    
import argparse
import Function

parser = argparse.ArgumentParser(description="Fill missing values using mean, mode and median methods")

parser.add_argument('-i', '--input', required=True, help="input file: house-prices.csv")
parser.add_argument('-m', '--method', required=True, help="accept only mean, mode and median")
parser.add_argument('-c', '--column', required=True, nargs='*', help= \
                    "must have at least one column, each column is separated by a white space")
parser.add_argument('-o', '--output', required=True, help="output file: output-{methodName}.csv")

args = parser.parse_args()

input, method, output = \
    args.input.lower(), args.method.lower(),  args.output.lower()

dataset = Function.loadData(input)
if (method == 'mean'):
    result = Function.fillMean(args.column, dataset, output)
    print(f"A {result} has been made")
elif (method == 'median'):
    result = Function.fillMedian(args.column, dataset, output)
    print(f"A {result} has been made")
elif (method == 'mode'):
    result = Function.fillMode(args.column, dataset, output)
    print(f"A {result} has been made")
else:
    print("Unknown method")

# print(args.input)
# print(args.method)
# print(args.column)
# print(args.output)

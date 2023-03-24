# Requirement: Delete duplicate samples.
# Argument syntax: python 6.py -i input.csv
# Example:         python 6.py -i house-prices.csv

import argparse
import Function

parser = argparse.ArgumentParser(description="Delete duplicate samples")

parser.add_argument('-i', '--input', required=True, help="input file: house-prices.csv")

args = parser.parse_args()

input = args.input.lower()

dataset = Function.loadData(input)

len_removeDup = Function.removeDuplicates(dataset)[0]
print(f"Length after removing duplicates: {len_removeDup}")
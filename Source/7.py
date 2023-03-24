# Requirement: Normalize a numeric attribute using min-max and Z-score methods.
# Argument syntax: python 7.py -i input.csv -m method -c column
# Example:         python 7.py -i house-prices.csv -m zscore -c LotFrontage

import argparse
import Function

parser = argparse.ArgumentParser(description="Normalize a numeric attribute using min-max and Z-score methods")

parser.add_argument('-i', '--input', required=True, help="input file: house-prices.csv")
parser.add_argument('-m', '--method', required=True, help="method: mm for min-max, zscore for z-score")
parser.add_argument('--min', help="new min", default=0)
parser.add_argument('--max', help="new max", default=0)
parser.add_argument('-c', '--column', required=True, help="choose a column to change (Note: please write the name of the column correctly)")
args = parser.parse_args()
        
input, method, newMax, newMin, col = \
    args.input.lower(), args.method.lower(), int(args.max), int(args.min), args.column
dataset = Function.loadData(input)

if (method == 'mm'):
    Function.minmax_normalization(dataset, newMax, newMin, col)
    # pass
elif (method == 'zscore'):
    Function.zscore_normalization(dataset, col)
else: 
    print("Invalid method")
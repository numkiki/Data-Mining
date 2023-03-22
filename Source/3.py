
# Example: python 3.py -i house-prices.csv -m mean -c LotArea Id -o output_mean.csv
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
    Function.fillMean(args.column, dataset, output)
    print("done mean")
elif (method == 'median'):
    Function.fillMedian(args.column, dataset, output)
    print("done median")
elif (method == 'mode'):
    Function.fillMode(args.column, dataset, output)
    print("done mode")
else:
    print("Unknown method")

# print(args.input)
# print(args.method)
# print(args.column)
# print(args.output)

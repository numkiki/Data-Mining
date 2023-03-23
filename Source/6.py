import argparse
import Function

parser = argparse.ArgumentParser(description="Fill missing values using mean, mode and median methods")

parser.add_argument('-i', '--input', required=True, help="input file: house-prices.csv")

args = parser.parse_args()

input = args.input.lower()

dataset = Function.loadData(input)

len_removeDup = Function.removeDuplicates(dataset)[0]
print(f"Length after removing duplicates: {len_removeDup}")
import argparse
import Function

parser = argparse.ArgumentParser(description="Fill missing values using mean, mode and median methods")

parser.add_argument('-m', '--method', required=True)
parser.add_argument('-c', '--column', required=True, nargs='*')
parser.add_argument('-o', '--output', required=True)

args = parser.parse_args()

# print(args.method)
# print(args.column)
# print(args.output)

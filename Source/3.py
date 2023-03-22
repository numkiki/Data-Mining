import argparse
import Function

parser = argparse.ArgumentParser(description="Fill missing values using mean, mode and median methods")

parser.add_argument('-i', '--input', required=True)
parser.add_argument('-m', '--method', required=True)
parser.add_argument('-c', '--column', required=True, nargs='*')
parser.add_argument('-o', '--output', required=True)

args = parser.parse_args()

input, method, output = \
    args.input.lower(), args.method.lower(),  args.output.lower()

dataset = Function.loadData(input)
if (method == 'mean'):
    Function.mean(args.column, dataset)
    pass
elif (method == 'median'):
    pass
elif (method == 'mode'):
    pass
else:
    print("Unknown method")

# print(args.input)
# print(args.method)
# print(args.column)
# print(args.output)

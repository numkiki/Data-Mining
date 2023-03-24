# Requirement: Performing addition, subtraction, multiplication, and division between two numerical attributes.
# Argument syntax: python 8.py -i input.csv -m method -c1 col1 -c2 col2
# Example:         python 8.py -i house-prices.csv -m a -c1 OverallQual -c2 OverallCond


import argparse
import Function

parser = argparse.ArgumentParser(description="Performing addition, subtraction, multiplication, and division between two numerical attributes")

parser.add_argument('-i', '--input', required=True, help="input file: house-prices.csv")
parser.add_argument('-m', '--method', required=True, help="a: addition, s: subtraction, m: multiplication, d: division")
parser.add_argument('-c1', '--col1', required=True, help="column 1")
parser.add_argument('-c2', '--col2', required=True, help="column 2")

args = parser.parse_args()

input, method, col1, col2 = \
    args.input.lower(), args.method.lower(), args.col1, args.col2
dataset = Function.loadData(input)

if (method == 'a'):
    result = Function.addition(dataset, col1, col2)
    print(result)
elif (method == 's'):
    result = Function.subtraction(dataset, col1, col2)
    print(result)
elif (method == 'm'):
    result = Function.multiplication(dataset, col1, col2)
    print(result)
elif (method == 'd'):
    result = Function.division(dataset, col1, col2)
    print(result)
else:
    print("Wrong method")
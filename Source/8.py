import argparse
import Function

parser = argparse.ArgumentParser(description="Fill missing values using mean, mode and median methods")

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
    if ".csv" in result:
        print(result)
    else: 
        print("Wrong attribute type")
elif (method == 's'):
    result = Function.subtraction(dataset, col1, col2)
    if ".csv" in result:
        print(result)
    else: 
        print("Wrong attribute type")    
elif (method == 'm'):
    result = Function.multiplication(dataset, col1, col2)
    if ".csv" in result:
        print(result)
    else: 
        print("Wrong attribute type")
elif (method == 'd'):
    result = Function.division(dataset, col1, col2)
    if ".csv" in result:
        print(result)
    else: 
        print("Wrong attribute type")
else:
    print("Wrong method")
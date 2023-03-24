import argparse
import Function

parser = argparse.ArgumentParser(description="Fill missing values using mean, mode and median methods")

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
    res = Function.minmax_normalization(dataset, newMax, newMin, col)
    if (res == True):
        print(f"3 new files have been created. The file to check is minmax_norm.csv")
    else:
        print("Wrong attribute type")
elif (method == 'zscore'):
    res = Function.zscore_normalization(dataset, col)
    if (res == True):
        print(f"3 new files have been created. The file to check is zscore_norm.csv")
    else:
       print("Wrong attribute type") 
else: 
    print("Invalid method")
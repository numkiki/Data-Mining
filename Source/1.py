"""
    Argument syntax:
        python 1.py input.csv
    Example:
         python 1.py house-prices.csv
"""


# Load the convenient packages
import sys
import Function
from pprint import  pprint
dataset = Function.loadData(sys.argv[1])

#Print result
print("Attribute are missed data:")
pprint(Function.listAttributes(dataset))
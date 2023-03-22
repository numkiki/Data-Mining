#  Deleting rows containing more than a particular number of missing values (Example: delete rows
#  with the number of missing values is more than 50% of the number of attributes).

# Load the convenient packages
import sys
import Function

dataset = Function.loadData(sys.argv[1])
rate = int(sys.argv[2].split("=")[1]) / 100
output = sys.argv[3].split("=")[1]

numAttributes = Function.numOfAttributes(dataset)
numMissing = Function.listNumOfMissing(dataset)
attributes = list(dataset.keys())

for attribute in attributes:
    if (numMissing[attribute] > (rate*numAttributes)):
        del dataset[attribute]

dataset.to_csv(output)
print("Attribute left after delete the missing value columns: ")
print(dataset.keys())
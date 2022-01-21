# tests for csv-to-latex

import csvtolatex as ctol

# Globals
# input list
inputCSV = ctol.csvListReader('Example_list2.csv')
# trim extra columns
inputCSV = ctol.trim(inputCSV)

# TESTS
print('Trimmed csv:')
for row in inputCSV:
    print(row)

print(f'number of columns = {ctol.numCols(inputCSV)}')

ctol.csvToLaTex(inputCSV, 'test2.txt', style=2, mode='w')

# print('Output of trimmed csv file: \n')
# for row in lTrimmed:
#     print(row)
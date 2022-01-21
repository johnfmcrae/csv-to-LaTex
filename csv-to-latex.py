# convert a csv fil to a LaTex table

# imports
# specify current directory to make sure debugger works correctly
import sys
sys.path.append('/Users/john/source/python_code/csv_to_LateX')
import csv

# input is the input file name
def csvListReader (input):
    with open(input, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

# define a function to trim extra commas
def trim(input):
    output = []
    for rows in input:
        rowOut = []
        for col in rows:
            if col != '': #: ) <3
                rowOut.append(col)
        output.append(rowOut)
    return output

def numCols(input):
    count = 0
    for elem in input:
        if len(elem) > count:
            count = len(elem)
    return count

"""
    Write LaTex style table

    INPUTS
    input - a list containing the csv contents,
            must be read into script before being passed in here
    file  - output file path, by default creates an output file
            called 'output.txt' in local directory
    style - choice of two output table types (see below),
            default is style 1
    mode  - write mode, either append, 'a', or write, 'w',
            the latter overwrites the content in the input file.
            default is 'a'

    Style 1 - basic tabular with centering:

    \begin{center}
    \begin{tabular}{c c}
        cell A1 & cell B1 \\
        cell A2 & cell B2
    \end{tabular}
    \end{center}

    Style 2 - table with [h!] float specifier
    
    \begin{table}[h!]
    \begin{center}
        \begin{tabular}{c c}
            cell A1 & cell B1 \\
            cell A2 & cell B2
        \end{tabular}
    \end{center}
    \end{table}

"""
def csvToLaTex(input, file = 'output.txt', style = 1, mode = 'a'):
    # determine number of columns
    cols = numCols(input)
    # open input file for reading
    if mode != 'a' and mode != 'w':
        print('Error, invalid write mode')
        return
    else:
        with open(file, mode) as file:
            # check style type
            if style == 1:
                # start table
                file.write('\\begin{center}\n\\begin{tabular}{')
                for i in range(cols):
                    if i != cols - 1:
                        file.write('c ')
                    else:
                        file.write('c}\n')
                # add the contents
                for rows in input:
                    file.write('\t')
                    for i in range(len(rows)):
                        if (i + 1) != len(rows):
                            file.write(f'{rows[i]} & ')
                        else:
                            file.write(f'{rows[i]}\\\\\n')
                # end the table
                file.write('\t\\end{tabular}\n\\end{center}\n')
            elif style == 2:
                pass
            else:
                print('Error, not a valid table style')
                return


# Globals
# input list
inputCSV = csvListReader('Example_list1.csv')
# trim extra columns
inputCSV = trim(inputCSV)

# TESTS
print('Trimmed csv:')
for row in inputCSV:
    print(row)

print(f'number of columns = {numCols(inputCSV)}')

csvToLaTex(inputCSV, 'test1.txt', style=1, mode='w')

# print('Output of trimmed csv file: \n')
# for row in lTrimmed:
#     print(row)

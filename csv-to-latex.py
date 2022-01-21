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
def trimmer(input):
    output = []
    for rows in input:
        rowOut = []
        for col in rows:
            if col != '': #: ) <3
                rowOut.append(col)
        output.append(rowOut)
    return output

# to be completed
def numCols(input):
    count = 0
    for elem in input:
        s = ''.join(elem)
        for c in s:
            pass

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
    # open input file for reading
    if mode != 'a' & mode != 'w':
        print('Error, invalid write mode')
        return
    else:
        with open(file, mode) as file:
                # check style type
            if style == 1:
                # TO DO: add {c c...} given colNums
                file.write('\\begin{center}\n\t\\begin{tabular}')
                # add the contents
                file.write('\t\\end{tabular}\n\\end{center}\n')
            elif style == 2:
                pass
            else:
                print('Error, not a valid table style')
                return


# Globals
# input list
inputCSV = csvListReader('Example_list1.csv')

# TESTS
print('Output of original csv file: \n')
for row in inputCSV:
    print(' '.join(row))

print('Output of trimmed csv file: \n')
for row in lTrimmed:
    print(row)

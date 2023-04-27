import math
import csv

def calculate(expression):
    try:
        expression = expression.replace('sin', 'math.sin')
        expression = expression.replace('cos', 'math.cos')
        expression = expression.replace('tan', 'math.tan')
        expression = expression.replace('^', '**')
        expression = expression.replace('pi', str(math.pi))
        result = eval(expression)
        return str(result)
    except:
        return 'Error'

# Read in the calculations from the CSV file
with open('calc_inputs.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # skip header row
    calculations = [row for row in reader]

# Perform the calculations and write the results to an output file
with open('results.txt', 'w') as outfile:
    for row in calculations:
        expression = row[0]
        result = calculate(expression)
        outfile.write(expression + ' = ' + result + '\n')
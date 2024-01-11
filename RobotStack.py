# Intro to Theory of Algorithms: Project 1
#
# Student Name: Ryan Stapf
# Date: 10/26/2023
#

# Used to read input.txt file from command prompt
import sys

# Used for base cases involving binomial coefficients
import math



# Wrapper Function
def robot_stack_memo_wrapper(b, n, k):
    
    # Base Case 1: if the stack limit is 1, the result is n choose b since this problem becomes a simple binomial coefficient
    if k == 1:
        combos = math.comb(n, b)
        return combos
    # Base Case 2: The smaller of the two values k or b will be the limiting factor. If b is the limiting factor, the result is (n + b - 1) chose b
    elif k >= b:
        combos = math.comb((n + b - 1), b)
        return combos
    # If the input does not meet any base case conditions, create a memoization dictionary to store the results and call the main function
    else:
        comboDict = {}
        return robot_stack_memo(b, n, comboDict)



# Main Function
def robot_stack_memo(b, n, comboDict):
    # There is only one combination for 0 bots and 0 spaces
    if n == 0 and b == 0:
        return 1
    # There cannot be a negative number of bots, therefore 0 is the sentinel value
    if n == 0 or b < 0:
        return 0
    # Prevents repetition of combination possibilites
    if (b, n) in comboDict:
        return comboDict[(b, n)]

    # Create a combination counter and initialize it to 0
    combos = 0

    # Iterate through the limiting variable (the smaller of the two between b or k)
    for i in range(0, min(b, k) + 1):
        # Recursively call the main function until it reaches a base case
        combos += robot_stack_memo(b - i, n - 1, comboDict)

    # Output the number of combinations
    comboDict[(b, n)] = combos
    return combos



# Open and parse text
inputFile = open(sys.argv[1], 'r')

# Create a list to store the values
line_list = []
inputVal = inputFile.readline().strip()
inputSplit = inputVal.split()

# Convert the numeric strings into integers
inputSplit = [int(numeric_string) for numeric_string in inputSplit]
line_list.append(inputSplit)

# Repeat for remaining lines in input.txt
while inputVal != '':
    inputVal = inputFile.readline().strip()
    inputSplit = inputVal.split()
    inputSplit = [int(numeric_string) for numeric_string in inputSplit]
    line_list.append(inputSplit)
line_list.pop()

# Print results by calling the function for each line of values
for line in line_list:
    b = line[0] # Total number of robots
    n = line[1] # Number of stacks
    k = line[2] # Max robots per stack
    combinations = robot_stack_memo_wrapper(b, n, k)
    answer = "({0},{1},{2}) = {3}".format(b, n, k, combinations)
    print(answer)

# Close the input file
inputFile.close()
# Find the missing number in a given list
def getMissingNumber(arr= [1, 2, 3, 4, 5, 7, 8, 9, 10],):
    n = len(arr);m = n + 1 # n+1 because it starts with 0 so need to add 1
    total = m * (m + 1) // 2 # formulae for sum of integers
    MissingNUm = total - sum(arr) # total - sum gives left over number
    print('The missing number is',MissingNUm )

getMissingNumber()


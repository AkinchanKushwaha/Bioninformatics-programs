# match = 1, mismatch = 0, indel = -1
import sys


def findAlignment(firstSequence, secondSequence):
    n = len(firstSequence)  # length of firstSequence
    m = len(secondSequence)  # length of secondSequence

    print("Length of first sequence is:", n, " \nLength of second sequence is:", m)

    # Initialization of dp matrix of size n+1 and m+1
    rows, cols = (n + 1, m + 1)
    dp = []

    # Traversing through whole dp matrix and assigning every element with 0
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(0)
        dp.append(col)

    # Initializing first row and column in decreasing order
    for i in range(0, n + 1):
        dp[i][0] = -1 * i
    for i in range(0, m + 1):
        dp[0][i] = -1 * i

    # Traversing from range 1 to n+1
    for i in range(1, n + 1):
        # Traversing from range 1 to m+1
        for j in range(1, m + 1):

            if firstSequence[i - 1] == secondSequence[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:
                dp[i][j] = max(dp[i - 1][j] - 1, dp[i][j - 1] - 1, dp[i - 1][j - 1])
    printMatrix(dp, firstSequence, secondSequence)

    # Replacing all the negative scores with 0
    for i in range(0, n + 1):
        for j in range(0, m + 1):
            if dp[i][j] < 0:
                dp[i][j] = 0

    printMatrix(dp, firstSequence, secondSequence)

    # maximum score in the matrix
    maxScore = -sys.maxsize - 1

    # index of maxScore
    maxScoreRow = 0
    maxScoreColumn = 0

    for i in range(0, n + 1):
        for j in range(0, m + 1):
            if dp[i][j] >= maxScore:
                maxScore = dp[i][j]
                maxScoreRow = i
                maxScoreColumn = j

    # counters for backtracking
    i = maxScoreRow
    j = maxScoreColumn

    print("i ", maxScoreRow, "j ", maxScoreColumn)

    # Initialization of two empty strings
    firstStringFinal = ""
    secondStringFinal = ""

    # variable to keep track of number of steps
    step = 0

    # Backtracking: Begin with the highest score, end when 0 is encountered.
    while i > 0 or j > 0:
        leftElement = dp[i][j - 1]
        topElement = dp[i - 1][j]
        diagonalElement = dp[i - 1][j - 1]
        currentElement = dp[i][j]

        if diagonalElement >= leftElement and diagonalElement >= topElement:
            firstStringFinal = firstSequence[i - 1] + firstStringFinal
            secondStringFinal = secondSequence[j - 1] + secondStringFinal
            i = i - 1
            j = j - 1


        elif currentElement == topElement:
            firstStringFinal = firstSequence[i - 1] + firstStringFinal
            secondStringFinal = "_" + secondStringFinal
            i = i - 1

        else:
            secondStringFinal = secondSequence[j - 1] + secondStringFinal
            firstStringFinal = "_" + firstStringFinal
            j = j - 1

        print("step:", step, firstStringFinal, " ", secondStringFinal)
        step += 1

    # print highlighted common sequence
    highlightMatchingSequence(firstStringFinal, secondStringFinal)


# function to highlight matching sequence of two sequence
def highlightMatchingSequence(firstString, secondString):
    BLUE = '\033[94m'
    END = '\033[0m'
    print("\nFinal matching sequence is: ")
    for i in range(len(firstString)):
        if firstString[i] == secondString[i]:
            print(BLUE, firstString[i], END, end="")
        else:
            print(firstString[i], END, end="")

    print()
    for i in range(len(secondString)):
        if firstString[i] == secondString[i]:
            print(BLUE, secondString[i], END, end="")
        else:
            print(secondString[i], END, end="")
    print()


# function to display a two dimensional function.
def printMatrix(arr, firstString, secondString):
    print("  _", end=" ")
    for i in range(len(secondString)):
        print(secondString[i], end=" ")
    print()
    for i in range(len(arr)):
        if i == 0:
            print("_", end=" ")
        else:
            print(firstString[i - 1], end=" ")
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()
    print()


if __name__ == '__main__':
    string1 = input("Enter first sequence: ")
    string2 = input("Enter second sequence: ")

    # Remove all the spaces from the string
    string1 = string1.upper().replace(" ", "")
    string2 = string2.upper().replace(" ", "")

    findAlignment(string1, string2)

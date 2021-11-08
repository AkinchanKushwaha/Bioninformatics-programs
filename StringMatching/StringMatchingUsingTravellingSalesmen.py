# ==========================================
#  Author: Akinchan Kushwaha
#  Date:   27 Oct 2021
# ==========================================


# function to find the maximum number of matches in two strings and common sequence between two strings
# using travelling salesmen algorithm.
def stringMatching(firstString, secondString):
    n = len(firstString)  # length of firstString
    m = len(secondString)  # length of secondString

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

    # Traversing from range 1 to n+1
    for i in range(1, n + 1):
        # Traversing from range 1 to m+1
        for j in range(1, m + 1):
            # If the characters of firstString and secondString match at position i and j then
            # current element(dp[i][j]) = 1 + diagonalElement(dp[i-1][j-1])
            #
            #   _ A G T C
            # _ 0 0 0 0 0
            # T 0 0 0 1 0
            # G 0 0 1 0 0
            # T 0 0 0 2 0
            # A 0 1 0 0 0
            #
            # In this example, value of current element is increased only when characters are same at index i and j.
            #
            if firstString[i - 1] == secondString[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

            # else if the characters of firstString and secondString don't match at position i and j then
            # current element(dp[i][j]) = maximum of topElement(dp[i][j-1]) and leftElement(dp[i-1][j]
            #
            #   _ A G T C
            # _ 0 0 0 0 0
            # T 0 0 0 1 1
            # G 0 0 1 1 1
            # T 0 0 1 2 2
            # A 0 1 1 2 2
            #
            # After applying both conditions, we get the above matrix.
            #
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # function call to display final matrix.
    printMatrix(dp, firstString, secondString)

    # Initialization of two empty strings
    firstStringFinal = ""
    secondStringFinal = ""

    # counters for backtracking
    i = n
    j = m

    # variable to keep track of number of steps
    step = 0

    # Backtracking in dp matrix.
    while i > 0 or j > 0:
        leftElement = dp[i][j - 1]
        topElement = dp[i - 1][j]
        diagonalElement = dp[i - 1][j - 1]
        currentElement = dp[i][j]

        # if diagonal element is greater than left and top element or
        # diagonal element is equal to both left and top element then
        # add character on present position to both strings.
        # if diagonal element is same as current element then it means
        # that characters at same index are not same and there's a mismatch
        if diagonalElement >= leftElement and diagonalElement >= topElement and diagonalElement != currentElement:
            firstStringFinal = firstString[i - 1] + firstStringFinal
            secondStringFinal = secondString[j - 1] + secondStringFinal
            i = i - 1
            j = j - 1

        elif i == 0 and j > 0:
            while j > 0:
                secondStringFinal = secondString[j - 1] + secondStringFinal
                firstStringFinal = "_" + firstStringFinal
                j = j - 1

        elif j == 0 and i > 0:
            while i > 0:
                firstStringFinal = firstString[i - 1] + firstStringFinal
                secondStringFinal = "_" + secondStringFinal
                i = i - 1

        elif i > 0 and currentElement == topElement:
            firstStringFinal = firstString[i - 1] + firstStringFinal
            secondStringFinal = "_" + secondStringFinal
            i = i - 1

        else:
            secondStringFinal = secondString[j - 1] + secondStringFinal
            firstStringFinal = "_" + firstStringFinal
            j = j - 1

        # print("step:", step, firstStringFinal, " ", secondStringFinal)
        step += 1

    # print highlighted common sequence
    highlightMatchingSequence(firstStringFinal, secondStringFinal)

    # Matching score of both string is dp[n][m]
    print("Matching score of both string is ", dp[n][m])


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

    stringMatching(string1, string2)

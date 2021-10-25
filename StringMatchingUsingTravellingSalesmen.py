# function to find the maximum number of matches in two strings using travelling salesmen algorithm.
def stringMatching(firstString, secondString):
    n = len(firstString)  # length of firstString
    m = len(secondString)  # length of secondString

    print("Length of first string is:", n, " \nLength of second string is:", m)

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

    # maximum number of matches in both string is dp[n][m]
    print("Maximum number of matching is ", dp[n][m])

    # function call to display final matrix.
    printMatrix(dp, firstString, secondString)


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


if __name__ == '__main__':
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")
    stringMatching(string1, string2)

def findBiggestRectangle(matrix: list[list[int]]) -> int:
    # Checks if matrix is empty
    if len(matrix) == 0:
        return 0

    # Initializes histogram
    histogram = [0 for _ in range(len(matrix[0]))]

    # Iterates for each row and creates histogram
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                histogram[j] += 1

    # Brute force calculations for the maxArea of the submatrix of all 1s
    # Iterates for each possible rectangle in the histogram
    maxArea = 0

    for i in range(len(histogram)):
        minHeight = histogram[i]
        for j in range(i, len(histogram)):
            minHeight = min(minHeight, histogram[j])
            currentArea = (j - i + 1) * minHeight
            maxArea = max(currentArea, maxArea)

    return maxArea

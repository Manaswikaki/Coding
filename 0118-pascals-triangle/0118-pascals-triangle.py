class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []

        for i in range(numRows):
            # Create a row of 1s with the appropriate length
            row = [1] * (i + 1)
            
            # Update the interior elements (exclude first and last)
            # Each element is the sum of the two elements above it
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            
            triangle.append(row)
            
        return triangle

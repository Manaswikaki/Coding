class Solution:
    def pushZerosToEnd(self, arr):
        # Write index for the position to place the next non-zero element
        write = 0

        # Move all non-zero elements forward
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[write] = arr[i]
                write += 1

        # Fill the remaining positions with zeros
        while write < len(arr):
            arr[write] = 0
            write += 1

        # The array is modified in place; return it if needed
        return arr
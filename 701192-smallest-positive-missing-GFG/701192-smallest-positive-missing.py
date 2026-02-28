class Solution:
    def missingNumber(self, arr):
        n = len(arr)

        # Place each number in its right place if possible
        for i in range(n):
            while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
                target = arr[i] - 1
                arr[i], arr[target] = arr[target], arr[i]

        # Find the first position where the value is not correct
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1

        # If all 1..n are present
        return n + 1
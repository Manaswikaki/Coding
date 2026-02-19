class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1  # n is the range limit, not the array size
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(arr)
        return expected_sum - actual_sum

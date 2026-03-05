class Solution:
    def maxIndexDiff(self, arr):
        n = len(arr)
        if n == 0:
            return 0

        # Build left_min: minimum value up to index i
        left_min = [0] * n
        left_min[0] = arr[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], arr[i])

        # Build right_max: maximum value from index j to end
        right_max = [0] * n
        right_max[-1] = arr[-1]
        for j in range(n - 2, -1, -1):
            right_max[j] = max(right_max[j + 1], arr[j])

        # Two-pointer scan to maximize j - i with left_min[i] <= right_max[j]
        i = 0
        j = 0
        max_diff = 0
        while i < n and j < n:
            if left_min[i] <= right_max[j]:
                max_diff = max(max_diff, j - i)
                j += 1  # try to increase distance
            else:
                i += 1  # left value too large, move left pointer

        return max_diff
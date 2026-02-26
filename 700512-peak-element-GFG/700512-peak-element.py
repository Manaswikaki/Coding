class Solution:
    def peakElement(self, arr):
        n = len(arr)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2

            left_neighbor = arr[mid - 1] if mid - 1 >= 0 else float('-inf')
            right_neighbor = arr[mid + 1] if mid + 1 < n else float('-inf')

            # Check if mid is a peak
            if arr[mid] > left_neighbor and arr[mid] > right_neighbor:
                return mid

            # If the right neighbor is greater, a peak lies to the right
            if arr[mid] < right_neighbor:
                left = mid + 1
            else:
                # Otherwise, peak lies to the left
                right = mid - 1

        return -1  # Should not happen for valid inputs
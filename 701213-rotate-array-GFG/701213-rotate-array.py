class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d %= n  # Handle cases where d > length
        
        # Slicing for Left Rotation: [d:] + [:d]
        # arr[:] ensures the original list is modified
        arr[:] = arr[d:] + arr[:d]
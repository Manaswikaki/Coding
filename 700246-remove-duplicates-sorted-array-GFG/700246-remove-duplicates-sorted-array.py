from typing import List

class Solution:
    def removeDuplicates(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        
        write = 1  # index to write the next unique element
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                arr[write] = arr[i]
                write += 1
        # Optional: truncate the array to the number of unique elements
        return arr[:write]
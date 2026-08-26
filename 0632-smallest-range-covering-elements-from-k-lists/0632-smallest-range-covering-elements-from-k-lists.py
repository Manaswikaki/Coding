import heapq

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        # Heap elements store: (value, list_index, element_index)
        min_heap = []
        current_max = float('-inf')
        
        # Initialize the heap with the first element of each list
        for i in range(len(nums)):
            val = nums[i][0]
            heapq.heappush(min_heap, (val, i, 0))
            current_max = max(current_max, val)
            
        # Track the global smallest range found
        ans_start, ans_end = float('-inf'), float('inf')
        
        while min_heap:
            current_min, list_idx, elem_idx = heapq.heappop(min_heap)
            
            # Check if current range is smaller than the best recorded range
            if current_max - current_min < ans_end - ans_start:
                ans_start, ans_end = current_min, current_max
                
            # If the current list has no more elements, we cannot proceed
            if elem_idx + 1 == len(nums[list_idx]):
                break
                
            # Fetch the next element from the same list and push to heap
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))
            current_max = max(current_max, next_val)
            
        return [ans_start, ans_end]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
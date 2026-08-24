import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count character frequencies
        counts = Counter(s)
        
        # Step 2: Build a Max-Heap (use negative values for Python's min-heap)
        max_heap = [[-cnt, char] for char, cnt in counts.items()]
        heapq.heapify(max_heap)
        
        # Check impossibility condition using the most frequent element
        if -max_heap[0][0] > (len(s) + 1) // 2:
            return ""
            
        res = []
        
        # Step 3: Process pairs of characters
        while len(max_heap) >= 2:
            cnt1, char1 = heapq.heappop(max_heap)
            cnt2, char2 = heapq.heappop(max_heap)
            
            res.append(char1)
            res.append(char2)
            
            # Re-add to heap if characters are still available
            if cnt1 + 1 < 0:
                heapq.heappush(max_heap, [cnt1 + 1, char1])
            if cnt2 + 1 < 0:
                heapq.heappush(max_heap, [cnt2 + 1, char2])
                
        # Step 4: Append the last remaining character if it exists
        if max_heap:
            res.append(max_heap[0][1])
            
        return "".join(res)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
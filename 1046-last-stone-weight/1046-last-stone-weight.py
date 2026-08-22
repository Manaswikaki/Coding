import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Invert weights to simulate a Max-Heap using Python's Min-Heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        # Smash stones until 0 or 1 stone remains
        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)
            
            if stone1 != stone2:
                # The difference (stone1 - stone2) is negative because weights are inverted
                heapq.heappush(max_heap, stone1 - stone2)
                
        return -max_heap[0] if max_heap else 0


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []
        
        for x, y in points:
            # Calculate squared Euclidean distance to avoid floating-point issues
            dist = x**2 + y**2
            
            # Python's heapq is a min-heap by default. 
            # Inverting the distance (-dist) turns it into a max-heap behavior.
            heapq.heappush(max_heap, (-dist, [x, y]))
            
            # If the heap size exceeds k, pop the element with the largest distance
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        # Return only the coordinate points from the remaining elements in the heap
        return [point for dist, point in max_heap]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
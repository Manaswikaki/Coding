import heapq

class MedianFinder:

    def __init__(self):
        # max-heap stores the smaller half (invert numbers to simulate max-heap)
        self.small = []
        # min-heap stores the larger half
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: Always push to small (max-heap) first
        heapq.heappush(self.small, -num)
        
        # Step 2: Ensure every element in small is <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # Step 3: Maintain size property (small can have at most 1 more element)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If odd number of elements, small heap holds the median
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        # If even, calculate average of the roots of both heaps
        return (-self.small[0] + self.large[0]) / 2.0


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # Initialize prices array with infinity
        prices = [float('inf')] * n
        prices[src] = 0
        
        # We can make at most k stops, which means at most k + 1 flights (edges)
        for _ in range(k + 1):
            # Create a copy to prevent updating a node and using that updated price 
            # within the same iteration (which would simulate more than 1 edge transition)
            tmp_prices = prices[:]
            
            for u, v, price in flights:
                if prices[u] == float('inf'):
                    continue
                if prices[u] + price < tmp_prices[v]:
                    tmp_prices[v] = prices[u] + price
                    
            prices = tmp_prices
            
        return prices[dst] if prices[dst] != float('inf') else -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
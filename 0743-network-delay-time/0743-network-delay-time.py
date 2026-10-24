import collections
import heapq


class Solution:

  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    # Build the adjacency list
    adj = collections.defaultdict(list)
    for u, v, w in times:
      adj[u].append((v, w))

    # Min-heap storing tuples of (time_elapsed, node)
    min_heap = [(0, k)]
    visit = set()
    total_time = 0

    while min_heap:
      time_elapsed, node = heapq.heappop(min_heap)

      # If the node is already visited, skip it
      if node in visit:
        continue
      visit.add(node)
      total_time = max(total_time, time_elapsed)

      # Explore neighbors
      for neighbor, weight in adj[node]:
        if neighbor not in visit:
          heapq.heappush(min_heap, (time_elapsed + weight, neighbor))

    # Return max time if all nodes are visited, else -1
    return total_time if len(visit) == n else -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
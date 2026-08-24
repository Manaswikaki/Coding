from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        counts = Counter(tasks)
        frequencies = list(counts.values())
        
        # Find the maximum frequency
        max_freq = max(frequencies)
        
        # Count how many tasks have this maximum frequency
        max_freq_count = frequencies.count(max_freq)
        
        # Calculate the minimum intervals required by the formula
        ans = (max_freq - 1) * (n + 1) + max_freq_count
        
        # The answer cannot be less than the total number of tasks
        return max(len(tasks), ans)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
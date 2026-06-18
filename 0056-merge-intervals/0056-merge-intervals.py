class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        # 1. Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            last_end = merged[-1][1]

            # 2. Check for overlap
            if current_start <= last_end:
                # Update the end of the last interval if current end is larger
                merged[-1][1] = max(last_end, current_end)
            else:
                # 3. No overlap, just append
                merged.append(intervals[i])

        return merged


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
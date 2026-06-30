class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Convert list to set for O(1) lookups
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Only start counting if 'num' is the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Continue the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
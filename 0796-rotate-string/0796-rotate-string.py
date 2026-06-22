class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # If lengths are different, s can never become goal
        if len(s) != len(goal):
            return False
        
        # Check if goal is a substring of s + s
        return goal in (s + s)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
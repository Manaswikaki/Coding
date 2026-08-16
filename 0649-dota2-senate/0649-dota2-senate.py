from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Store indices of senators in separate queues
        radiant = deque()
        dire = deque()
        
        n = len(senate)
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
                
        # Simulate the voting process round by round
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            
            # The senator with the smaller index bans the other
            # The winner goes to the next round (current index + n)
            if r_idx < d_idx:
                radiant.append(r_idx + n)
            else:
                dire.append(d_idx + n)
                
        return "Radiant" if radiant else "Dire"


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        # code here
        a=list(map(int, str(n)))
        c=0
        for i in a:
            if i==0:
                continue
            if n%i==0:
                c+=1
        return c        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
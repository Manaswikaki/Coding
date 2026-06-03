#User function Template for python3

class Solution:
	def reverseDigits(self, n):
		su=0
		# Code here
		while n !=0:
		    r=n%10
		    su=su*10+r
		    n=n//10
		return su    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
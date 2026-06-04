class Solution:
    def isPalindrome(self, n):
		# code here
		n=abs(n)
		a=n
		s=0
		while n!=0:
		    r=n%10
		    s=s*10+r
		    n=n//10
		if s == a:
		    return True
		else:
		    return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
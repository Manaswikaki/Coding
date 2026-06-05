class Solution:
    def isPrime(self, n):
        # 1 or less are not prime
        if n <= 1:
            return False
        # 2 and 3 are prime
        if n <= 3:
            return True
        # Eliminate multiples of 2 and 3
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        # Check from 5 to sqrt(n), skipping even numbers
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
            
        return True


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
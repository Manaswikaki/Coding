class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Initialize a boolean array "isPrime" and set all entries to True.
        # isPrime[i] will be False if i is not a prime, True otherwise.
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if isPrime[i]:
                # Mark multiples of i starting from i*i as False.
                # Multiples less than i*i would have already been marked.
                for multiple in range(i * i, n, i):
                    isPrime[multiple] = False
        
        # The number of True values in the array is the count of primes.
        return sum(isPrime)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
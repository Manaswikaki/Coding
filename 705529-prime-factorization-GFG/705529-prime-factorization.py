class Solution:
    def printPrimeFactorization(self, n):
        # Start with the smallest prime
        i = 2
        
        # Trial division up to n
        while i * i <= n:
            while n % i == 0:
                # Print factor followed by a space
                print(i, end=" ")
                n //= i
            i += 1
            
        # If n is still > 1, it's a prime factor
        if n > 1:
            print(n, end=" ")
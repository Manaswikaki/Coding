class Solution:
    def isPrime(self, n):
        # 1 and below are not prime numbers
        if n <= 1:
            return False
        
        # Check for divisors from 2 to sqrt(n)
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
            
        return True

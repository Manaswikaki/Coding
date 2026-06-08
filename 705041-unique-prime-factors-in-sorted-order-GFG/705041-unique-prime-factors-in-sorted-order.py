class Solution:
    def primeFac(self, n):
        # code here
        fact=[]
        while n%2==0:
            fact.append(2)
            n//=2
        for i in range(3,int(n**0.5)+1,2):
            while n%i==0:
                fact.append(i)
                n//=i
        if n>2:
            fact.append(n)
        res=list(set(fact))
        res.sort()
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
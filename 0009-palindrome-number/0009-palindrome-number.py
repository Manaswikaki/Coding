class Solution:
    def isPalindrome(self, x: int) -> bool:
        b=x
        x=abs(x)
        a=x
        s=0
        while x!=0:
            r=x%10
            s=s*10+r
            x=x//10
        n=(s==a)
        if b<0:
            n=False    
        if n:
            res= True
        else:
            res= False        
        return res    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
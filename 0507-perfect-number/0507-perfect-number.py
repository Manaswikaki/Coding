class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        l=[]
        for i in range(1,num):
            if num%i==0:
                l.append(i)
        t=sum(l)        
        if t==num:
            return True
        else:
            return False    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
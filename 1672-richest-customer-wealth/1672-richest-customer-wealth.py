class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        le=len(accounts)
        l = []
        for i in range(0,le):
            t=sum(accounts[i])
            l.append(t)
        return max(l)    
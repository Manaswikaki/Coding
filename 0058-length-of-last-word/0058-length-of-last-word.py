class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.strip().split()
        res=len(a[-1])
        return res
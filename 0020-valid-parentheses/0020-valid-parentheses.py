class Solution:
    def isValid(self, s: str) -> bool:
        # Mapping of closing to opening brackets
        pair = {')': '(', ']': '[', '}': '{'}
        # Stack to keep track of opening brackets
        stack = []
        
        for ch in s:
            if ch in pair.values():  # opening bracket
                stack.append(ch)
            elif ch in pair:         # closing bracket
                if not stack or stack[-1] != pair[ch]:
                    return False
                stack.pop()
            else:
                # If there were other characters (not expected per constraints)
                return False
        
        return not stack
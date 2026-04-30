class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        # Sort to handle duplicates and allow early pruning
        candidates.sort()
        
        def backtrack(remain, start, path):
            if remain == 0:
                # Target reached
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                # If the current number is greater than the remaining sum, stop the loop
                if candidates[i] > remain:
                    break
                
                # Skip duplicate elements at the same depth to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                # Move to the next index (i + 1) because each number is used once
                backtrack(remain - candidates[i], i + 1, path)
                path.pop() # Backtrack

        backtrack(target, 0, [])
        return res

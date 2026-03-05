from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results: List[List[int]] = []
        candidates.sort()  # Optional: helps pruning and ensures non-decreasing order in combos

        def dfs(start: int, remaining: int, path: List[int]):
            # If remaining is exactly 0, we found a valid combination
            if remaining == 0:
                results.append(path.copy())
                return
            # If remaining becomes negative, this path cannot be a solution
            if remaining < 0:
                return

            # Explore candidates starting from 'start' to allow unlimited use of the same candidate
            for i in range(start, len(candidates)):
                cur = candidates[i]
                # Pruning: since candidates are sorted, if cur > remaining, no need to continue
                if cur > remaining:
                    break

                # Include cur and continue exploring with the same i (since we can reuse)
                path.append(cur)
                dfs(i, remaining - cur, path)
                path.pop()  # backtrack

        dfs(0, target, [])
        return results
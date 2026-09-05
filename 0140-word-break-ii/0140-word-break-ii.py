class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        memo = {}

        def backtrack(start: int) -> list[str]:
            # If we've already computed the results for this suffix, return it
            if start in memo:
                return memo[start]
            
            # Base case: reached the end of the string
            if start == len(s):
                return [""]
            
            res = []
            # Explore all possible word cuts from the current start index
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # Get all valid sentences formed by the remaining suffix
                    sub_sentences = backtrack(end)
                    for sub in sub_sentences:
                        if sub == "":
                            res.append(word)
                        else:
                            res.append(word + " " + sub)
            
            memo[start] = res
            return res

        return backtrack(0)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # Convert list to set for O(1) lookups
        wordSet = set(wordList)
        
        # If the destination word is not in the list, no path exists
        if endWord not in wordSet:
            return 0
        
        # Queue stores tuples of (current_word, level_length)
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, length = queue.popleft()
            
            # If we reached the target word, return the step count
            if word == endWord:
                return length
            
            # Try changing each character of the word
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    
                    # If the transformed word is valid
                    if next_word in wordSet:
                        # Remove from set to act as a 'visited' check
                        wordSet.remove(next_word)
                        queue.append((next_word, length + 1))
                        
        return 0


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
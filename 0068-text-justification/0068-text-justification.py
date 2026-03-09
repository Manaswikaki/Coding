from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res: List[str] = []
        i = 0
        n = len(words)

        while i < n:
            # Determine how many words fit on the current line
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            # Words from i to j-1 are on this line
            line_words = words[i:j]
            num_words = len(line_words)

            # If this is the last line or the line contains a single word
            if j == n or num_words == 1:
                # Left-justify: join with single spaces and pad on the right
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                # Fully justify: distribute spaces as evenly as possible
                total_chars = sum(len(w) for w in line_words)
                total_spaces = maxWidth - total_chars
                slots = num_words - 1  # gaps between words

                # Base spaces per slot and extra spaces to distribute to the left
                space_base, extra = divmod(total_spaces, slots)

                line_parts = []
                for k in range(num_words - 1):
                    line_parts.append(line_words[k])
                    # add space for this slot
                    spaces = space_base + (1 if k < extra else 0)
                    line_parts.append(" " * spaces)
                line_parts.append(line_words[-1])  # last word
                line = "".join(line_parts)

            res.append(line)
            i = j

        return res
class Solution:
    def isNumber(self, s: str) -> bool:
        # Helper to skip leading/trailing spaces if you want to allow them.
        # The problem states only certain chars appear, so we won't strip spaces.
        i, n = 0, len(s)

        if n == 0:
            return False

        # Track required components after parsing
        seen_digit = False       # any digit in mantissa
        seen_dot = False         # dot in mantissa
        seen_exp = False         # exponent introduced
        sign_allowed = True      # sign allowed at current position

        def scan_digits(idx: int) -> int:
            # Consume digits starting at idx, return new index
            j = idx
            while j < n and s[j].isdigit():
                j += 1
            return j

        # 1) optional sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            i += 1

        # 2) mantissa: either digits with optional dot, or dot with digits
        mantissa_digits = False

        # digits before dot
        j = scan_digits(i)
        if j > i:
            mantissa_digits = True
            seen_digit = True
            i = j

        # dot handling
        if i < n and s[i] == '.':
            if seen_dot:
                return False
            seen_dot = True
            i += 1

            # digits after dot
            j = scan_digits(i)
            if j > i:
                mantissa_digits = True
                seen_digit = True
                i = j
        # If no digits yet and there was a dot but no digits around, invalid (e.g., ".")
        if not mantissa_digits:
            return False

        # 3) exponent part
        if i < n and (s[i] == 'e' or s[i] == 'E'):
            if seen_exp:
                return False
            seen_exp = True
            i += 1

            # exponent sign
            if i < n and (s[i] == '+' or s[i] == '-'):
                i += 1

            # must have at least one digit in exponent
            exp_start = i
            j = scan_digits(i)
            if j == exp_start:
                return False
            i = j

        # trailing chars must be consumed
        return i == n
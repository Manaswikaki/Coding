class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def backtrack(index, path, current_val, prev_operand):
            # Base case: reached end of string
            if index == len(num):
                if current_val == target:
                    res.append(path)
                return

            for j in range(index, len(num)):
                # Handle leading zeros: '0' is okay, but '05' is not
                if j > index and num[index] == '0':
                    break
                
                # Get the current substring and its integer value
                sub_str = num[index : j + 1]
                val = int(sub_str)

                if index == 0:
                    # First number, no operator needed
                    backtrack(j + 1, sub_str, val, val)
                else:
                    # Addition
                    backtrack(j + 1, path + "+" + sub_str, current_val + val, val)
                    # Subtraction
                    backtrack(j + 1, path + "-" + sub_str, current_val - val, -val)
                    # Multiplication: undo prev_operand, then add (prev_operand * val)
                    backtrack(j + 1, path + "*" + sub_str, 
                              (current_val - prev_operand) + (prev_operand * val), 
                              prev_operand * val)

        backtrack(0, "", 0, 0)
        return res

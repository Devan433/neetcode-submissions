class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for ch in s:
            if ch not in pairs:  # opening bracket
                stack.append(ch)
            else:  # closing bracket
                if not stack or stack[-1]!=pairs[ch]:
                    return False
                stack.pop()

        return not stack
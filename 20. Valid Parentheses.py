class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                try:
                    if d[ch] != stack.pop():
                        return False
                except IndexError:
                    return False
        return True if len(stack) == 0 else False

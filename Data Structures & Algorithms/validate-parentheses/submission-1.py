class Solution:
    def isValid(self, s: str) -> bool:
        characterMap = {'}':'{', ')':'(', ']':'['}
        stack = []

        for c in s:
            if c in characterMap:
                if stack and stack[-1] == characterMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in hash:
                if stack and stack[-1] == hash[ch]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(ch)

        return not stack
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        for i in range(n):
            temp = s[i:n] + s[0:i]
            if temp == goal:
                return True
        return False
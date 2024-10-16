class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', ']':'[', '}':'{'}
        stack = []
        for char in s:
            if char in mapping.values():
                stack.append(char)
                
            elif char in mapping.keys():
                if stack == [] or mapping[char] != stack.pop():
                    return False
        return stack == []
            
        
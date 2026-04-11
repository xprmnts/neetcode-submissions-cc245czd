class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {']': '[', ')': '(', '}': '{'}
        stack = ['#'] 
        
        for c in s:
            if c in paren_map:
                if paren_map[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 1
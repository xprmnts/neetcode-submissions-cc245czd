class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {']':'[',')':'(','}':'{'}
        stack = []

        for c in s:
            if c in paren_map:
                top_element = stack.pop() if stack else '#'
                
                if paren_map[c] != top_element:
                    return False
            else:
                stack.append(c)
        return not stack
                
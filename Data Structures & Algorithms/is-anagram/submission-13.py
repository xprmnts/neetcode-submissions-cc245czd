class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        if len(s) != len(t):
            return False
        
        alpha = [0] * 26

        for idx in range(len(s)):
            char_s_idx = ord("a") - ord(s[idx])
            char_t_idx = ord("a") - ord(t[idx])
            alpha[char_s_idx] += 1
            alpha[char_t_idx] -= 1
        
        return all(x == 0 for x in alpha)

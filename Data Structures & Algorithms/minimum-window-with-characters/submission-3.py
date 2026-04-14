from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        # maps
        count_t = collections.Counter(t)
        count_w = collections.Counter()

        # vars
        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("inf")
        l = 0

        for r, char in enumerate(s):
            # window
            if char in count_t:
                count_w[char] += 1
                if count_w[char] == count_t[char]:
                    have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                left_char = s[l]
                if left_char in count_t:
                    count_w[left_char] -= 1
                    if count_w[left_char] < count_t[left_char]:
                        have -= 1

                l += 1
        
        l, r = res
        return s[l: r + 1] if res_len != float("inf") else ""
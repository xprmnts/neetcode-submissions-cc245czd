from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        count_t = Counter(t)
        window = {}
        
        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("inf")
        l = 0

        for r, char in enumerate(s):
            if char in count_t:
                window[char] = window.get(char, 0) + 1
                if window[char] == count_t[char]:
                    have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                left_char = s[l]
                if left_char in count_t:
                    window[left_char] -= 1
                    if window[left_char] < count_t[left_char]:
                        have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""
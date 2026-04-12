class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        count_t, window = collections.Counter(), collections.Counter()

        for c in t:
            count_t[c] += 1
        
        have, need = 0, len(count_t)
        result, result_len = [-1, -1], float("infinity")
        l = 0
        for r, c in enumerate(s):
            window[c] += 1

            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < result_len:
                    result = [l, r]
                    result_len = (r - l + 1)
                
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
            
        l, r = result
        return s[l:r+1] if result_len != float("infinity") else ""
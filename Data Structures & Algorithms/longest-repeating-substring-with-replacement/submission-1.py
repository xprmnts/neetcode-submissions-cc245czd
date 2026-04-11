class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.Counter()
        res = 0
        l = 0
        max_f = 0

        for r, char in enumerate(s):
            count[char] += 1

            max_f = max(max_f, count[char])

            if (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
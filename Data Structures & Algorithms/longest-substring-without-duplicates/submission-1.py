class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in last_seen:
                l = max(last_seen[s[r]] + 1, l)
            last_seen[s[r]] = r
            res = max(res, r - l + 1)
        return res
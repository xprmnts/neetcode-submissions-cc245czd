class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        left = 0

        while left < len(s):
            right = s.find("#", left)
            length = int(s[left:right])
            left = right + 1
            res.append(s[left:left + length])
            left += length
        return res

            


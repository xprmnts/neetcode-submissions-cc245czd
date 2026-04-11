class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)
        

    def decode(self, s: str) -> List[str]:
        res = []
        left = 0

        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
            length = int(s[left:right])
            left = right + 1
            right = left + length
            res.append(s[left:right])
            left = right
        return res

            


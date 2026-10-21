class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            length = len(word)
            res += str(length)
            res += "#"
            res += word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            length = int(length) 
            str_idx = i + length 
            i += 1 
            word = ""
            while i <= str_idx:
                word += s[i]
                i += 1
            res.append(word)
        return res
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1 = [0] * 26
        m2 = [0] * 26
        for c in s:
            m1[ord(c) - ord('a')] += 1
        for c in t:
            m2[ord(c) - ord('a')] += 1
        if m1 == m2:
            return True
        else:
            return False
            
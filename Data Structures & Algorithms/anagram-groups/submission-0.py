class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for word in strs:
            mp1 = [0] * 26
            for chr in word:
                mp1[ord(chr) - ord('a')] += 1
            mp1 = tuple(mp1)
            if mp1 in mp:
                mp[mp1].append(word)
            else:
                mp[mp1] = [word]
        return list(mp.values())
        
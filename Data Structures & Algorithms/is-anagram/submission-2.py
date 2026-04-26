class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for c in s:
            count[c] = count.get(c,0) + 1
        
        for c in t:
            count[c] = count.get(c, 0) - 1

        for i in count.values():
            if i != 0:
                return False
        return True
    
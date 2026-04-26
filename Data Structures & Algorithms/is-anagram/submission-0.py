class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char1 = []
        char2 = []

        for i in s:
            char1.append(i)

        for j in t:
            char2.append(j)

        if sorted(char1) == sorted(char2):
            return True
        else:
            return False
    
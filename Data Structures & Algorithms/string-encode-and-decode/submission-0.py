class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ''
        for i in strs:
            length = len(i)
            encode += f'{length}#{i}'

        return encode


    def decode(self, s: str) -> List[str]:
        i = 0
        decode = []

        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            decode.append(word)
            i = j+1+length
        return decode
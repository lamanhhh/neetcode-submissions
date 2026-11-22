class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ''
        for s in strs:
            ret += str(len(s)) + '@'  + s

        return ret

    def decode(self, s: str) -> List[str]:
        ret = []

        n = len(s)

        i = 0

        while i < n:
            
            start = s.index('@', i)
            num = int(s[i:start])
            end = start + 1 + num

            ret.append(s[start + 1:end])

            i = end
            
        return ret
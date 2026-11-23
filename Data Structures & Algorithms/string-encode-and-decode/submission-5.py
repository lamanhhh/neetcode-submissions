class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ''
        
        for s in strs:
            ret += str(len(s)) + '#' + s
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []

        i = 0
        while i < len(s):
            idx = s.index('#', i)
            start = idx + 1
            
            string_len = int(s[i:start - 1])
            end = start + string_len
            ret.append(s[start:end])

            i = end

        return ret

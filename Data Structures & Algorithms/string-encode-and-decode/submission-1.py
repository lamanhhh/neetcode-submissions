class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''

        for s in strs:
            result += str(len(s)) + ':' + s

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        
        i = 0


        while i < len(s):
            colon = s.index(':', i)
            num = int(s[i:colon])

            start = colon + 1
            end = colon + 1 + num

            result.append(s[start:end])

            i = end

        return result
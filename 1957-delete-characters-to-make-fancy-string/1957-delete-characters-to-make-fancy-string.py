class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []

        for ch in s:
            if len(result) < 2 or not (result[-1] == result[-2] == ch):
                result.append(ch)

        return ''.join(result)
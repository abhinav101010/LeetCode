class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = {}

        for i in range(len(word)):
            upperChar = word.find(word[i].upper())
            if word[i].islower() and upperChar > i:
                ans.update({word[i]: upperChar})
            if word[i] in ans.keys() and upperChar < i:
                ans.pop(word[i])
        return len(ans)
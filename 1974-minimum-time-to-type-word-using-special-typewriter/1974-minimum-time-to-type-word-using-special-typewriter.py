class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        curr = 0  # Position of 'a'

        for ch in word:
            target = ord(ch) - ord('a')
            distance = abs(target - curr)
            time += min(distance, 26 - distance) + 1
            curr = target

        return time
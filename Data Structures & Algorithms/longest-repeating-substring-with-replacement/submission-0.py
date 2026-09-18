class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # char: count
        left = 0
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            max_frequency = max(max_frequency, max(count.values()))

            while (right - left + 1) - max_frequency > k:
                count[s[left]] = count.get(s[left], 0) - 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
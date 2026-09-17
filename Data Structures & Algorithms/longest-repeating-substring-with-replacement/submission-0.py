class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        maxfreq = 0
        maxlen = 0

        for r in range(len(s)):

            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1

            maxfreq = max(maxfreq , count[s[r]])

            while (r - l + 1) - maxfreq > k:
                count[s[l]] -= 1
                l += 1

            maxlen = max(maxlen , r - l + 1)
        return maxlen        
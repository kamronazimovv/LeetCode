class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0 
        left = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                left = max(left, r - l +1)
            seen[char] = r
        return left
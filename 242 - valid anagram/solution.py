# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        for c in s:
            if c not in s_hash:
                s_hash[c] = 1
            else:
                s_hash[c] += 1
        for c in t:
            if c not in t_hash:
                t_hash[c] = 1
            else:
                t_hash[c] += 1
        return s_hash == t_hash

print(Solution().isAnagram("ratt", "tartar"))

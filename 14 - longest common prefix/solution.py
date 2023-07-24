from typing import List

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      longest_prefix = strs[0]
      for str in strs:
        if longest_prefix == '':
          return ''
        else:
          new_longest_prefix = ''
          for i, c in enumerate(longest_prefix):
            if i < len(str):
              if longest_prefix[i] != str[i]: 
                break
              else:
                new_longest_prefix += str[i]
          longest_prefix = new_longest_prefix
      return longest_prefix
          
         



print(Solution().longestCommonPrefix(['cart', 'car', 'card']))
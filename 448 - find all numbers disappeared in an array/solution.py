from typing import List

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash = {}
        max = len(nums)
        r = range(1, max + 1)
        list = []
        for n in nums:
            hash[n] = True
        for n in r:
            if n not in hash:
                list.append(n)
        return list

print(Solution().findDisappearedNumbers([1, 2, 3, 4, 6, 2]))
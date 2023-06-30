from typing import List

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        most_freq = []
        for n in nums:
            if n not in hash:
                hash[n] = 1
            else:
                hash[n] += 1
        while len(most_freq) < k:
            highest_freq = 0
            for p in hash:
                if hash[p] > highest_freq:
                    highest_freq = hash[p]
            for p in hash:
                if hash[p] == highest_freq:
                    most_freq.append(p)
                    hash[p] = 0
        return most_freq
        

print(Solution().topKFrequent([1, 1, 1, 2, 2, 3, 3, 3, 3], 2))
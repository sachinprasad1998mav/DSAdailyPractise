#  Top K Frequent Elements
# Solved
# Medium
# Topics
# Companies

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

 

# Constraints:

#     1 <= nums.length <= 105
#     -104 <= nums[i] <= 104
#     k is in the range [1, the number of unique elements in the array].
#     It is guaranteed that the answer is unique.


class Solution:
    def topKFrequent(self, nums, k):
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        freq = [[] for i in range(len(nums)+1)]
        for key, value in d.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq)-1, -1, -1):
            for j in sorted(freq[i]):  # Sort the elements at each frequency level
                res.append(j)
                if len(res) == k:
                    return res
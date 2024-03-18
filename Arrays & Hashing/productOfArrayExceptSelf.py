# Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


# Algorithm:
# the base idea is if we can have a array to store the products of numbers less the respective index, and greater than the index, we can multioly and find the res.


# testcase:
# nums =     [1,2,3,4]

# pre =      [1,1,2,6]

# post =     [24,12,4,1]

# res =      [24,12,8,6]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        print(pre)

        post = [1] * len(nums)
        for i in range(len(nums)-2,-1,-1):
            post[i] = post[i+1] * nums[i+1]
        print(post)

        res = [pre[i]*post[i] for i in range(len(nums))]
        return res
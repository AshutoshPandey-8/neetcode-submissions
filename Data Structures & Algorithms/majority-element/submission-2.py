class Solution:
    def majorityElement(self, nums):
        return max(set(nums),key=nums.count)
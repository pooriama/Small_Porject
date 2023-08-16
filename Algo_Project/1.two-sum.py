#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictadd={}

        for i in range(len(nums)):
            dictadd[target-nums[i]]=i
        
        for i in range(len(nums)):
            if nums[i] in dictadd and i!=dictadd[nums[i]]:
                return i,dictadd[nums[i]] 

# @lc code=end

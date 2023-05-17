#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_dict:
                return [nums_dict[diff], i]
            nums_dict[num] = i
        
# @lc code=end


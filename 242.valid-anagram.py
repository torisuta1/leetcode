#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return True if sorted_s == sorted_t else False


        
# @lc code=end


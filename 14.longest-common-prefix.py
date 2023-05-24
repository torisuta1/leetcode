#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = min(strs)
        max_str = max(strs)
        matched_str = ""
        for str in min_str:
            if max_str.startswith(matched_str + str):
                matched_str += str
            else:
                break
        return matched_str 
        


        
# @lc code=end


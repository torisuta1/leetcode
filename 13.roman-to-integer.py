#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        char_list = [0]
        comparison_list = [0]
        for i, char in enumerate(s):
            if char == "I" : tmp = 1 
            if char == "V" : tmp = 5 
            if char == "X" : tmp = 10 
            if char == "L" : tmp = 50 
            if char == "C" : tmp = 100 
            if char == "D" : tmp = 500 
            if char == "M" : tmp = 1000 
            if comparison_list[i] >= tmp:
                char_list.append(tmp)
                comparison_list.append(tmp)
            if comparison_list[i] < tmp:
                char_list.append(tmp - char_list[i] * 2)
                comparison_list.append(tmp)
        return sum(char_list)

        

# @lc code=end


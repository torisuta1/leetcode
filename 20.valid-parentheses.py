#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_dict = {")": "(", "}": "{", "]": "["}
        for s in s:
            if not stack: 
                stack.append(s)
                continue
            if s == ")" and stack[-1] == parentheses_dict[s]:
                stack.pop(-1)
                continue
            if s == "}" and stack[-1] == parentheses_dict[s]: 
                stack.pop(-1)
                continue
            if s == "]" and stack[-1] == parentheses_dict[s]: 
                stack.pop(-1)
                continue
            stack.append(s)
        return True if not stack else False
                
                


        

# @lc code=end


#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for char in operations:
            if char == "+":
                stack.append(stack[-1] + stack[-2])
                continue
            if char == "D":
                stack.append(stack[-1] * 2)
                continue
            if char == "C":
                stack.pop()
                continue
            stack.append(int(char))
        return sum(stack)
                

        
# @lc code=end


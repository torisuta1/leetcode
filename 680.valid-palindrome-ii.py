#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                skipL = s[left + 1:right + 1]
                skipR = s[left:right]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            left, right = left +1, right -1
        return True
        
# @lc code=end


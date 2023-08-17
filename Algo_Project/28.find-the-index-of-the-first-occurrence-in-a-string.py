#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#
# algorithms
# Easy (40.13%)
# Likes:    4413
# Dislikes: 230
# Total Accepted:    1.9M
# Total Submissions: 4.7M
# Testcase Example:  '"sadbutsad"\n"sad"'
#
# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.
# 
# 
# Example 1:
# 
# 
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# 
# 
# Example 2:
# 
# 
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= haystack.length, needle.length <= 10^4
# haystack and needle consist of only lowercase English characters.
# 
# 
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:


        def checkneedle(needle,haystack,i):
            if needle==haystack[i:i+len(needle)]:
                return i
            else:
                return -1
            


        result=-1
        for i in range(len(haystack)-len(needle)+1):
            if needle[0]==haystack[i]:
                result=checkneedle(needle,haystack,i)
                if result!=-1:
                    return i
                
        return -1
# @lc code=end


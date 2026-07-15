# LeetCode 242
# Valid Anagram
# Difficulty: Easy
# Time: O(n)
# Space: O(n)

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        dic = {}
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i], 0) + 1
            dic[t[i]] = dic.get(t[i], 0) - 1
        
        for i in dic.values():
            if i != 0:
                return False
        
        return True
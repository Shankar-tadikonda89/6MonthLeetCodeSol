# LeetCode 217
# Contains Duplicates
# Difficulty: Easy
# Time: O(n)
# Space: O(n)

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
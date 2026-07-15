# LeetCode 128
# Longest Consecutive Sequence
# Difficulty: Medium
# Time: O(n)
# Space: O(n)

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        maxLen = 0

        for num in nums:
            if num-1 in nums:
                continue
            else:
                count = 0
                current = num

                while current in nums:
                    current += 1
                    count += 1
                
                maxLen = max(maxLen, count)
        
        return maxLen
# LeetCode 1
# Two Sum
# Difficulty: Easy
# Time: O(n)
# Space: O(n)


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in dic:
                return [i, dic[complement]]
            
            dic[nums[i]] = i
        
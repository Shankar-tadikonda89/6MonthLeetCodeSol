# LeetCode 49
# Group Anagrams
# Difficulty: Medium
# Time: O(n x k)
# Space: O(n)

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        dic = {}

        for i in strs:
            l = [0] * 26

            for j in i:
                l[ord(j) - ord('a')] += 1
            
            search = tuple(l)
            if search not in dic:
                dic[search] = []
            dic[search].append(i)
        
        return list(dic.values())
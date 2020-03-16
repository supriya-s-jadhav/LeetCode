"""
This script will take list of numbers and return the indices of two numbers that add up the target number.
Given nums = [2, 7, 11, 15], target = 9,
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if(nums):
            dic = {}
            for index, num in enumerate(nums):
                temp = target - num
                if temp in dic:
                    return(dic[temp],index)
                dic[num]=index

if __name__ == "__main__":
    nums=[-3,-2,-6]
    target=-8
    s1=Solution()
    s1.twoSum(nums,target)

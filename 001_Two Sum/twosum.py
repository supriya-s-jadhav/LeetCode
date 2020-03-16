"""
This script will take list of integer numbers and target integer number. It will return the indices of two numbers that add up the target number.
Ex: Given nums = [-3,-2,-4], target = -6
    Output: [1,2]
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

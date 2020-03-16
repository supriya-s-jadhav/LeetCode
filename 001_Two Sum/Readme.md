# Two Sum

## Problem Statement

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Example

Key: We need to return the index of numbers that add up to the target value.
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Expected Input :

```
Given nums = [2, 7, 11, 15], target = 9,
```

```
return [0, 1].
```
## My Solution

My preferred solution can be found in twosum.py file in [001_Two Sum directory](https://github.com/supriya-s-jadhav/LeetCode/blob/master/001_Two%20Sum/twosum.py)

## Possible Solutions

Different Simple solutions in python. Brute force solution takes

1. Brute Force

```
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if (nums):
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    sum = nums[i] + nums[j]
                    if (sum == target):
                        return(i,j)
s1=Solution()
s1.twosum([2, 7, 11, 15],9)
```

2. Hash map

```
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index, num in enumerate(nums):
            if num in dic:
                return [dic[num], index]
            dic[target - num] = index

```
# TWO SUM
# Given an array of intergers, return indices of the two numbers such that they add to a specific target
# You may assume that each input would have exactly on solution, and you may not use the same element twice

# Example 1: Given nums = [2,7,11, 15], target = 9
# Because nums[0] + nums[1] = 2 + 7 = 9 , return [0, 1]

#Example 2:
# Given nums = [2,1,5,3], target = 4

Time: O(n)
Memory: O(n)

class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        prevMap = {} #Value : Index

        for i, n in enumerate(nums): #If difference is already in the hashMap
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i] # Return a pair of indices 
            prevMap[n] = i 
        return

#MAXIMUM SUBARRAY

#Given an integer array, find the contiguos subarray (containing at least one number) which has the largest sum and return its sum

#Example:

#Input: [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explain: [4,-1,2,1] has the largest sum = 6

#Code

class solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

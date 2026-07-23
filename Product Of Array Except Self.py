#Product Of Array Except Self

#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]
#The product of any prefix or suffix of nums is guaranteed fit in a 32- bit integer
#You must write an algorithm that runs in O(n) time and without using the division operation

#Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

#Code
class solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix #Take each position in the output array and put the prefix
            prefx *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):#Go back to the begining
            res[i] *= postfix
            postfix *= nums[i]
        return res #Return the output array results

    #Time: O(n)
    #Memory: O(1)

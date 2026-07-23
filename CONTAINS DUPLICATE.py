#CONTAINS DUPLICATE

#Given an integer array nums, return true if any value appears at least twice in the arraym and return false if element is distint

#Example 1 
#Input: nums = [1,2,3,1]
#Output: True 

#Example 2:
#Input : nums = [1,1,1,3,3,4,3,2,4,2]
#Output : True

#Code

class solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() #Create the hashset

        for n in nums:
            if n in hashset: #Is n a duplicate
                return True
            hashset.add(n)
        return false

#Time: O(n)
#Space: O(n)

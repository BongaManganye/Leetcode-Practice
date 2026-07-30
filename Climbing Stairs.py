#Climbing Stairs - Dynamic Programming

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1 #Initialize these two variables by one

        for i in range(n - 1):
            temp = one #Put one in a temporary variable
            one = one + two #Updating one
            two = temp #Shifting two in the temp variable

        return one
#Time: O(n)

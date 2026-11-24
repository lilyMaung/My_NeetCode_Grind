class Solution:
    def climbStairs(self, n: int) -> int:
        #Given: an integer n where n represents the number of steps to reach the top of a staircase, we can climb either 1 or 2 steps at a time
        #Output: return the number of distinct ways to climb to the top of the staircase
        
        
        #we need base cases
        if n == 1:
            return 1
        
        if n == 2:
            return 2

        #We have to remember our steps
        #if u take one step, you only need one step to move forward
        oneStepBack = 2
        #if u take two steps, you need 1 times 2 steps to move forward
        twoStepback = 1

        #starting from stair 3 we are climbing our way through til n
        #For n = 5, range(3, 6) gives 3, 4, 5, which is three passes. That matches the trace from before
        for current in range (3, n+1):
            #sum of two previous steps
            current = oneStepBack + twoStepback
            twoStepback = oneStepBack
            oneStepBack = current
    

        return oneStepBack


"""
Runtime - O(n) because I loop once through the stairs. Space is O(1) because I only keep the last two values instead of a full table.
If I were to use recursion or DP array then space would be O(n)

"""


        
        
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Given: An array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase
        #After paying the cost, we can step to either the (i+1)th floor or the (i+2)th floor
        #we can choose either index 0 or 1 floor
        #Output: return the minimum cost to reach the top of the staircase
       
        #to remember the cost
        oneStepBack = 0
        twoStepBack = 0
        
        #now we counting the min Cost to get to the top
        #we have to loop through until len(cost)+1 because python would exclude it
        for i in range(2, len(cost)+1):
            #in each step we have to calculate we have to calculate the sum of how much we paid to get here + how much will it cost to leave here        # cost[i-1] is paid to leave cost and min
            fromOneBack = oneStepBack + cost[i-1]
            fromTwoBack = twoStepBack + cost[i-2]

            #we take whichever minimum
            current = min(fromOneBack, fromTwoBack)

            # we have to move forward
            twoStepBack = oneStepBack
            oneStepBack = current
            

        return oneStepBack


        """

        Runtime- len of the cost which is n so it's O(n)
        Space - O(1) because we only use two variables 

        """








        
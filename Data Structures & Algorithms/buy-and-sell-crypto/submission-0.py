class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #we are starting from day zero and the first thing we see will be our minimum before the loop
        ourMin = prices[0]
        #initializing
        bestProfit = 0

        #now we are trasversing the array from first day
        for n in range(1, len(prices)):
            #we have to calculate the profit everytime we loop through
            profitToday = prices[n] - ourMin

            #then we have to compare and see if we made more profit or not and take the more profit
            bestProfit = max(bestProfit, profitToday)
            #the more profit we need, the less mininum it has to be
            ourMin = min(ourMin, prices[n])
        
        return bestProfit
        


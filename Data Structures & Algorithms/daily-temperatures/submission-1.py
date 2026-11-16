class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #given an array of integers as temperatures
        #each index value represents the daily temperatures on that index day 
        # to return the number of days where you found the warmer temperature than your current index one

        #getting the result array by setting everything to zero
        n = len(temperatures)
        result = [0] * n
        stack = []
        #Optimized way
        #first we need to scan the array and push it onto the stack
        for j, temp in enumerate(temperatures):
            #doing until the stack is not empty
            while stack and temperatures[stack[-1]] < temp:
                #if less than then pop all the temp on the stack that are less than temp
                i = stack.pop()

                result[i] = j -i
            stack.append(j)
        return result
            
            







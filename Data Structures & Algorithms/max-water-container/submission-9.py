class Solution:
    def maxArea(self, height: list[int]) -> int:
        #Given: an array height of length n, n is the vertical lines drawn that the two endpoints of the ith line are (i,0)and (i,height[i])

        #to find two lines that together with the x axis form a containter, so that the container contains most water
        #Output- return the maximum amount of water a contaienr can store

        # array value is the height, and each index represents a vertical line
        # so we have to find the maximum area of the container
        # height * width = area
        # height is height[i] 
        # width is the difference between two vertical lines meaning two pointers

        #two pointers
        left = 0
        right=  len(height)-1
        maxArea =0
        #start looping through the array

        while left < right:
            # everytime we loop, we have to calculate the area and keep track of it
            width = right - left
            # when we are considerign the height we can only take whichever the shorter cause water cannot pass that line
            ourHeight = min(height[right], height[left])

            area = width * ourHeight
            #if there is greater area then we keep track of it
            maxArea = max(area, maxArea)
            if height[left]<height[right]:
                left +=1
            else:
                right -=1
        
        return maxArea

    #FINALLY SOLVED THIS PROBLEM WITHOUT AI HELP, DEBUGGING ON MY OWN IN 13 MINS, PROUD OF MYSELF

    # Time complexity: O(n)
    # Space O(min(n, k)) whether we have the whole string without any repeating characters or k which is the alphabet size



        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #We have to return the maximum possible area by multiplying width and height of two bars
        #so we need two pointers one from the front and one from the back

        front = 0
        back = len(heights) -1

        maxArea = 0

        while front < back:
            #we will calculate the area of the container, if we need more area then we would move forward the front, else the back forward
            #minimum of the height because that height will determine how much water could contain
            totalArea = (back-front) * min(heights[front], heights[back])
            
            maxArea = max(maxArea, totalArea)

            if heights[front] < heights[back]:
                front +=1
            elif heights[front]>heights[back]:
                back -=1
            else:
                front +=1
                back-=1
            
        return maxArea
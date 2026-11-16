class Solution:
    def maxArea(self, heights: List[int]) -> int:
        front = 0
        back = len(heights) - 1
        max_area = 0

        #writing this function to find the minimum
        def min(num1, num2):
            if num1<= num2:
                return num1
            else:
                return num2
               
        while front < back:
            area = (back - front) * min(heights[front], heights[back] )
            #if we find the bigger area then we update the area
            if area > max_area:
                max_area = area

            elif heights[front] <= heights[back]:
                front +=1
            else:
                back -=1

        return max_area

            

        
            
            



            
        
                




        






        
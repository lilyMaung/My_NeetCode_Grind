class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #we have to set the pointers
        front =0
        back = len(heights) -1
        # to keep track of the max area
        max_area =0

        while front < back:
            #area = width * the lower bar
            #the lower bar will limit our amount of water that we can store
            #so we have to keep finding the taller bar
            area = (back-front) * min(heights[front],heights[back])

            #we only keep track of max area
            if area > max_area:
                max_area = area
            # if it's lower then we need to move the shorter bar forward or backward
            elif heights[front]<=heights[back]:
                front +=1
            else:
                back -=1
        return max_area

        
            

    



        
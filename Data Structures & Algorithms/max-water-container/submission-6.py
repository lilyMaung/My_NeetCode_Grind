class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        front =0
        back = len(heights) -1 
        max_area=0

        while front < back:
            area = (back - front) * min(heights[front], heights[back])

            if area > max_area:
                max_area = area

            elif heights[front]<= heights[back]:
                front +=1

            else:
                back -=1

        return max_area

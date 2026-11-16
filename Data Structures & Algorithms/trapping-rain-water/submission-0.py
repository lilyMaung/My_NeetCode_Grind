class Solution:
    def trap(self, height: List[int]) -> int:
       # you have two pointers from the front and back 
       # but for this it's not only two bars but every bar matters
       # we have to calculate water trapped between each bar and take count of it
        front = 0
        back = len(height)-1
        water = 0
        frontMax = backMax = 0
        backMax = 0

        while front < back:
            #so we have to find the tallest from the front and the tallest from the back
           
            if height[front] < height[back]:
                frontMax = max(height[front], frontMax)
                water += frontMax - height[front]
                front +=1
            else: 
                backMax = max(height[back], backMax)
                water += backMax - height[back]
                back -=1
            
                
            
        return water

                
               


            
    
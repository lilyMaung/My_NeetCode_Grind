class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #converging pointers
        front = 0
        back = len(numbers)-1

        #this is a sorted array so it should be converging pointers

        while front < back:
            ourSum = numbers[front] + numbers[back]

            if ourSum == target:
                return [front+1, back+1]
            # okay so the front is the smallest and the back is the largest
            # [1,2,3,4] if 1+4=5 and target is 6 
            #That means front has to be bigger
            elif ourSum < target:
                front +=1
            elif ourSum > target:
                back -=1
            

        
    
            


                    
            

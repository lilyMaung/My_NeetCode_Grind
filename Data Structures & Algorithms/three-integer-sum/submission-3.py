from typing import List
# have to def solve this problem again
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #we need to sort the array first 
        nums.sort()
        result = []

        # we need to skip the duplicates
        
        for i in range(len(nums)-1):
            right = len(nums)-1
            left = i + 1

        
            #skipping the duplicates
            if i>0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                ourSum = nums[i]+ nums[left]+ nums[right]

                if ourSum < 0:
                    left +=1
                
                elif ourSum > 0:
                    right -=1
                
                else:
                    result.append([nums[i], nums[left],nums[right]])
                    #then we move both pointers
                    left +=1
                    right -=1

                    while left < right and nums[left]==nums[left-1]:
                        left +=1
                        
                    while left < right and nums[right]==nums[right+1]:
                        right -=1
                
        return result

                    
        



      
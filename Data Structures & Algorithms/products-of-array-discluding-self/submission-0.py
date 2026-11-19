class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #goal is to solve this in O(n)

        prefix = 1
        suffix = 1

        answer = [1] * len(nums)

        # Prefix - going from right to left
        for i in range(len(nums)):
            answer[i] = prefix 
            prefix = prefix * nums[i]
        
            
        # Suffix - going from right to left
        for i in range(len(nums)-1, -1 , -1):
            answer[i] = answer[i] * suffix
            suffix = suffix * nums[i]
        
        return answer


#HAVE TO DO THIS PROBLEM UNDERSTAND
        

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # goal was to return false if we see any value that appears more than once in the array
        #using something like a set would be good to clear out duplicates
        mySet = set()

        #looping through the array
        for num in nums:
            if num in mySet:
                return True
            else:
                mySet.add(num)
        
        return False



       
           

        
        
        
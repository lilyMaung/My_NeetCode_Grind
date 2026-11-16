class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we need a hashmap first

        seen = {}
      

        # goal is to return the index of the two numbers that sum up to the target
        for i, num in enumerate(nums):
            complement = target - num

            # if the number we lookihng for is in the seen then we returned if not we don't return
            if complement in seen:
                return [seen[complement], i]

            seen[num] = i





        


        

        
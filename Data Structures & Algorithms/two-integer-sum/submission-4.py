class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myNum ={}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in myNum:
                return [myNum[complement], i]

            myNum[num] = i

    
    
        
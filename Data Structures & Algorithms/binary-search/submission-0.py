class Solution:
    def search(self, nums: list[int], target: int) -> int:
        #Given: an array of integers nums which is sorted in ascending order
        # integer target
        # To write a function to search target in nums
        #if target exists, then return its index, or else return -1

        #MUST BE O(LOG N)

        #which means we cannot go through each item 
        # so we have to compare the root with the target and if the target is greater than right tree else left tree

        #we need left and right

        left, right = 0, len(nums)-1 

        while left <= right:
            # mid point
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left =mid+1
            else:
                right = mid-1
            mid = -1
            
        return -1


    """
    Time complexity - O(log n) cause we are dividing
    Space - O(1)
    """

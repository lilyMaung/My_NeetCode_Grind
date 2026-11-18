class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        #Given : an integer matrix m x n
        # each row is sorted in ascending order
        #the first integer of each row is greater than the last integer of the previous row
        # given the target, return true if target is in matrix or else false

        # it has to be in O(log(m*n))
        # m is row and n is column

        #the size of the flattern out matrix which is row * colum -1
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m * n - 1

        while left <= right:

            mid = left + (right - left) // 2

            row = mid // n

            col = mid % n

            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] < target:
                left = mid +1
            
            else:
                right = mid -1
            
        return False

        








        return False


    """

    Remember how to calculate row and column when flattern out

    Time is O(log m * n) 
    Space is O(1)

    """



        

        
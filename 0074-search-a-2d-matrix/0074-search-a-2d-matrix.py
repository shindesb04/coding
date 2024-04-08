class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        m = row - 1
        n = 0

        while 0 <= m < row and  0 <= n < col:
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] > target:
                m -= 1
            else:
                n += 1
        return False
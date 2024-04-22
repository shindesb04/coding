class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        row = len(grid)
        col = len(grid[0])

        def countOne(r, c, row, col):
            
            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
            cnt = 0
            for i, j in directions:
                nr = r + i
                nc = c + j
                if 0 <= nr < row and 0 <= nc < col:
                    if grid[nr][nc] == 1:
                        cnt += 1
            if cnt == 0:
                return 4
            elif cnt == 1:
                return 3
            elif cnt == 2:
                return 2
            elif cnt == 3:
                return 1
            else:
                return 0

        visited = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count += countOne(i, j, row, col)
        return count
        
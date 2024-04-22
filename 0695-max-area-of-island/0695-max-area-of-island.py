class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        maxarea = 0
        visited = set()
        row, col = len(grid), len(grid[0])
        count = 0

        def island(r, c, row, col):

            q = deque()
            q.append((r,c))
            visited.add((r,c))
            area = 0
            
            while q:
                area += 1
                directions = [[1,0], [-1,0], [0, -1], [0, 1]]
                i, j = q.popleft()
                for r, c in directions:
                    nr = r + i
                    nc = c + j
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))
                    
            return area

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = island(i, j, row, col)
                    maxarea = max(maxarea, area)
                    
        return maxarea

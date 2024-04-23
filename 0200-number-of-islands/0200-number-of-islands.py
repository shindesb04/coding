class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        visited = set()
        row, col = len(grid), len(grid[0])

        def island(r, c, row, col):
            q = deque()
            q.append((r, c))
            visited.add((r,c))

            while q:
                directions = [[1,0], [-1,0], [0, 1], [0, -1]]
                r, c = q.popleft()
                for i, j in directions:
                    nr = r + i
                    nc = c + j

                    if  0 <= nr < row and 0 <= nc < col and (nr, nc) not in visited and grid[nr][nc] == "1":
                        visited.add((nr,nc))
                        q.append((nr, nc))
                        


        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i, j) not in visited:
                    island(i, j, row, col)
                    count += 1
        return count
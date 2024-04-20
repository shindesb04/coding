class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        R, C = len(grid), len(grid[0])
        q = deque()

        flag = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1 or grid[i][j] == 2:
                    flag = 1
        if flag == 0:
            return 0 
        #mark all the rotten oranges

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q.append([i,j])
        
        time = -1
        #check the queue and mark the adjacent sides as rotten too
        while q:
            
            size = len(q)
            direction = [[1,0], [-1,0], [0,1], [0,-1]]
            for i in range(size):
                j, k = q.popleft()
                
                for r,c in direction:
                    row = r + j
                    col = c + k
                    if (0 <= row < R and 0 <= col < C) and (grid[row][col] == 1):
                        grid[row][col] = -1
                        q.append([row,col])
            
            time += 1
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    return -1
        return time

        
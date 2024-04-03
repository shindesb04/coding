class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        extra = [[0 for i in range(n)] for j in range(m)]
        direction = [[1,0],[0,1],[0,-1],[-1,0],[-1,-1],[1,1],[1,-1],[-1,1]] 
        for i in range(m):
            for j in range(n):
                count = 0
                
                for r, c in direction:
                    r = r + i
                    c = c + j
                    if 0 <= r < m and 0 <= c < n:
                        if board[r][c] == 1 or board[r][c] == -2:
                            count += 1
                if (board[i][j] == 1 or board[i][j] == -2) and (count < 2 or count > 3):
                    board[i][j] = -2
                elif (board[i][j] == 0 or board[i][j] == -1) and (count == 3):
                    board[i][j] = -1
        for i in range(m):
            for j in range(n):
                if board[i][j] == -2:
                    board[i][j] = 0
                if board[i][j] == -1:
                    board[i][j] = 1
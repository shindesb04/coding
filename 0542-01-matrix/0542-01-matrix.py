class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        q = deque()
        visited = set()

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    visited.add((i, j))
                    q.append((i,j))
        time = 0
        while q:
            time += 1
            size = len(q)
            for i in range(size):
                directions = [[1,0], [-1,0], [0,1], [0, -1]]
                r, c = q.popleft()
                for i, j in directions:
                    nr = r + i
                    nc = c + j
                    if 0 <= nr < row and 0 <= nc < col and mat[nr][nc] == 1 and (nr, nc) not in visited:
                        mat[nr][nc] = time
                        visited.add((nr,nc))
                        q.append((nr,nc))
        return mat
        
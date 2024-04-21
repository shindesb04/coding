class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color:
            return image
        intialcolor = image[sr][sc]
        ROW = len(image)
        COL = len(image[0])

        def dfs(R, C, ROW, COL, intialcolor):
            #base case
            if image[R][C] == color or image[R][C] != intialcolor:
                return
            if image[R][C] == intialcolor:
                image[R][C] = color
                        

            #logic
            direction = [[1,0], [-1,0], [0,-1], [0,1]]
            for r,c in direction:
                nr = r + R
                nc = c + C
                if 0 <= nr < ROW and 0 <= nc < COL:
                    dfs(nr, nc, ROW, COL,intialcolor)
                
        dfs(sr, sc, ROW, COL, intialcolor)
        return image

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 0000 - 0100 - 0200 - 0210 - 0211 - 0212 - 0202

        # 0000 - 0001 - 0002

        q = deque()
        q.append(("0000", 0))
        stage = 0

        search = set()
        for ele in deadends:
            search.add(ele)
        if "0000" in search:
            return -1

        while q:
            size = len(q)
            stage += 1
            cur, moves = q.popleft()
            
            if cur == target:
                return moves
            #0000
            for j in range(len(cur)):
                single = int(cur[j])
                add = (single + 1) % 10
                newcomb = cur[:j] + str(add) + cur[j+1:]
                if newcomb not in search:
                    search.add(newcomb)
                    q.append((newcomb, moves + 1))
                minus = ((single - 1) + 10) % 10
                newcomb = cur[:j] + str(minus) + cur[j+1:]
                if newcomb not in search:
                    search.add(newcomb)
                    q.append((newcomb, moves + 1))

        return -1
                    


                    
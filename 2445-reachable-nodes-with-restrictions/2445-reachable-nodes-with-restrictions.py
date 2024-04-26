class Solution:
    count = 0
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        self.count = 0
        rest = defaultdict(list)
        for one, two in edges:
            rest[one].append(two)
            rest[two].append(one)
        
        count = 0
        q = deque([0])
        visited = set()
        restricted = set(restricted)
        while q:
            count += 1
            element = q.popleft()
            visited.add(element)
            val = rest[element]
            for v in val:
                if v not in restricted and v not in visited:
                    q.append(v)
        return count

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites:
            return True

        countmap = [0 for i in range(numCourses)]
        dependency = defaultdict(list)
        q = deque()
        count = 0
        for one, two in prerequisites:
            countmap[one] += 1
            if two in dependency:
                dependency[two].append(one)
            else:
                dependency[two] = [one]

        for num in range(numCourses):
            if countmap[num] == 0:
                count += 1
                q.append(num)
        
        if not q:
            return False

        while q:
            element = q.popleft()
            temp = dependency[element]
            if temp:
                for i in range(len(temp)):
                    countmap[temp[i]] = countmap[temp[i]] - 1
                    if countmap[temp[i]] == 0:
                        count += 1
                        q.append(temp[i])
                        if count == numCourses:
                            return True

        return False
        
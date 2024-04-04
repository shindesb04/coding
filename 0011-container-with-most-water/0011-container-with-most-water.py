class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxwater = 0
        while l < r:
            water = min(height[l], height[r]) * (r - l)
            maxwater = max(maxwater, water)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxwater
        
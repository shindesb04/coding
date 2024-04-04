class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in number:
                return [number[nums[i]], i]
            else:
                number[diff] = i
        
        return [0,0]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        count = 1
        lent = len(nums)
        for i in range(len(nums)):
            if i-1 >= 0 and nums[i] == nums[i - 1]:
                count += 1
            elif i - 1 >= 0 and nums[i] != nums[i-1]:
                count = 1
            if count <= 2:
                nums[slow] = nums[i]
                slow += 1
        return slow

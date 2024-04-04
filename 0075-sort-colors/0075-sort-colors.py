class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, h = 0, len(nums) - 1
        m = 0
        while m <= h:
            if nums[m] == 2:
                nums[h], nums[m] = nums[m], nums[h]
                h -= 1
            elif nums[m] == 0:
                temp = nums[l]
                nums[l] = nums[m]
                nums[m] = temp
                l += 1
                m += 1
            else:
                m += 1
        
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total = m + n - 1
        first = m - 1
        second = n - 1
        
        if second < 0:
            return

        while first >= 0 and second >= 0:
            if nums1[first] > nums2[second]:
                nums1[total] = nums1[first]
                first -= 1
            else:
                nums1[total] = nums2[second]
                second -= 1
            total -= 1
        
        if first >= 0:
            while first >= 0:
                nums1[total] = nums1[first]
                first -= 1
                total -= 1
        if second >= 0:
            while second >= 0:
                nums1[total] = nums2[second]
                second -= 1
                total -= 1
        
        
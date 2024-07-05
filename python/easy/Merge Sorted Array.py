class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        it_1 = m - 1
        it_2 = n - 1
        it_3 = m + n -1

        while it_1 >= 0 and it_2 >= 0:
            if nums1[it_1] <= nums2[it_2]:
                nums1[it_3] = nums2[it_2]
                it_2 -= 1
                it_3 -= 1
            else:
                nums1[it_3] = nums1[it_1]
                it_1 -= 1
                it_3 -= 1

        while it_2 >= 0:
            nums1[it_3] = nums2[it_2]
            it_2 -= 1
            it_3 -= 1

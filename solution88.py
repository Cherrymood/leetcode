class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:(len(nums1))] = nums2[0:n]
        nums1.sort()

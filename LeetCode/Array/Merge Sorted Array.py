class Solution(object):
    def merge(self, nums1, m, nums2, n):
        del nums1[m:]
        nums1 += nums2[0:n]
        nums1.sort()
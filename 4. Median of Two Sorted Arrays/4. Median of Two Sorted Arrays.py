class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        result=sorted(nums1)
        result_len=len(result)
        result_len_half=int(result_len/2)
        if result_len % 2 ==0:
            median=(result[result_len_half]+result[result_len_half-1])/2
        else:
            median =result[result_len_half]
        return median
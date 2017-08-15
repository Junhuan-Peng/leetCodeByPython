class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = sorted(nums1 + nums2)
        length = len(nums3)
        result = -1
        if length % 2 == 0:
            mid = int(length / 2)
            result = (nums3[mid] + nums3[mid - 1]) / 2
        else:
            mid = int(length / 2)
            result = nums3[mid]
        return result

if __name__ == '__main__':
    s = Solution()
    assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5, 'Error'

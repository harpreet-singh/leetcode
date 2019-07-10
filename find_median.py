class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        k = 0
        l = 0
        t = []
        l1 = len(nums1)
        l2 = len(nums2)
        for i in nums1:
            while k < l2:
                if i < nums2[k]:
                    t.append(i)
                    l+=1
                    break
                else:
                    t.append(nums2[k])
                    k+=1
        
        if k < l2:
            t.extend(nums2[k:])
        if l < l1:
            t.extend(nums1[l:])

        mid =(l1+l2)//2
        
        return (t[mid] + t[~mid] )/2

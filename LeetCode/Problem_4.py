# Problem 4 : Median of Two Sorted Arrays (Hard)

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

# Answer:

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1+=nums2
        print(nums1)
        nums1.sort()
        print(nums1)
        size=len(nums1)
        if(size%2==0):
            med1= nums1[size//2]
            med2=nums1[size//2-1]
            return (med1+med2)/2
        else :
            return nums1[(size-1)//2]

a =Solution()
print(a.findMedianSortedArrays([1,3],[2,4]))
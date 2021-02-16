# Leetcode 4 - Median of Two Sorted Arrays
# Level: HARD
# O(log(min(M,N))) time, O(1) space

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        
        middle = (m + n + 1) // 2
        min_idx, max_idx = 0, m
        
        while min_idx <= max_idx:
            i = (min_idx + max_idx) // 2
            j = middle - i
            if i > 0 and nums1[i-1] > nums2[j]: 
                max_idx = i - 1
            elif i < m and nums2[j-1] > nums1[i]: 
                min_idx = i + 1
            else: 
                # Found a solution here
                break
        
        if i == 0: max_left = nums2[j-1]
        elif j == 0: max_left = nums1[i-1]
        else: max_left = max(nums1[i-1], nums2[j-1])
        
        # If (m + n) is odd
        if (m + n) % 2 == 1: 
            return max_left
        
        # If (m + n) is even
        if i == m: min_right = nums2[j]
        elif j == n: min_right = nums1[i]
        else: min_right = min(nums1[i], nums2[j])
        
        return (max_left + min_right) / 2

# Driver code
if __name__ == '__main__':
    nums1, nums2 = [1, 2], [3]
    median = Solution().findMedianSortedArrays(nums1, nums2)
    print("Median from nums1 and nums2:", median)
    
    nums1, nums2 = [1,2], [3,4]
    median = Solution().findMedianSortedArrays(nums1, nums2)
    print("Median from nums1 and nums2:", median)
    
    nums1, nums2 = [0,0], [0,0]
    median = Solution().findMedianSortedArrays(nums1, nums2)
    print("Median from nums1 and nums2:", median)      
    
    nums1, nums2 = [], [1] 
    median = Solution().findMedianSortedArrays(nums1, nums2)
    print("Median from nums1 and nums2:", median)
    
    nums1, nums2 = [2], []
    median = Solution().findMedianSortedArrays(nums1, nums2)
    print("Median from nums1 and nums2:", median)
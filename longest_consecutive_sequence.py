# Leetcode 128 - Longest COnsecutive Sequence
# Level: HARD
# O(N) time, O(N) space

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      numset = set(nums)
      max_length = 0
    
      for num in numset:
        if num-1 in numset:
            continue
        
        seq = 0
        while num in numset:
            seq += 1
            num += 1
            
            max_length = max(max_length, seq)
        
      return max_length

# Driver code
if __name__ == '__main__':
    nums1 = [100,4,200,1,3,2]
    longest = longestConsecutive(nums1)
    print("Longest consecutive sequence length: ", longest)
    
    nums2 = [0,3,7,2,5,8,4,6,0,1]
    longest = longestConsecutive(nums2)
    print("Longest consecutive sequence length: ", longest)
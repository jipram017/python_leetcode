# Leetcode 132 - Palindrome Partitioning II
# Level: HARD
# O(N**2) time, O(N) space

class Solution:
    def minCut(self, s: str) -> int:
        min_cuts = [i - 1 for i in range(len(s) + 1)]
        for i in range(len(s)):
            # Find odd palindrome
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                min_cuts[right + 1] = min(min_cuts[right + 1], 1 + min_cuts[left])
                left -= 1
                right += 1
            
            # Find even palindrome
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                min_cuts[right + 1] = min(min_cuts[right + 1], 1 + min_cuts[left])
                left -= 1
                right += 1    
                
        return min_cuts[-1]           
        
# Driver code
if __name__ == '__main__':
    string1 = "aab"
    minCut = Solution().minCut(string1)
    print(minCut)
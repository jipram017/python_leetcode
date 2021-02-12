# Leetcode 340 - Longest Substring with At Most K Distinct Characters
# Level: HARD
# O(N) time, O(1) space

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        start, longest = 0, 0
        last_seen = {}
        
        for i, c in enumerate(s):
            last_seen[c] = i
            while len(last_seen) > k:
                if last_seen[s[start]] == start:
                    del last_seen[s[start]]
                start += 1
            
            if (i-start+1) > longest:
                longest = i-start+1
                res = (start, i)
        
        return longest, s[res[0]:res[1]+1]

# Driver code
if __name__ == '__main__':
    input1 = "abcadcacacaca"
    k = 3      
    longest = Solution().lengthOfLongestSubstringKDistinct(input1, k)
    print("Longest substring from input1:", longest)
    
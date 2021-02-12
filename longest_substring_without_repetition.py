# Leetcode 3 - Longest Substring Without Repeating Characters
# Level: MEDIUM
# O(N) time, O(1) space

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        start, longest = 0, 0
        
        for i, c in enumerate(s):
            if c in last_seen and last_seen[c] >= start:
                start = last_seen[c] + 1
            else:
                longest = max(longest, i - start + 1)
            last_seen[c] = i
        
        return longest

# Driver code
if __name__ == '__main__':
    input1 = "abcabcbb"
    longest = Solution().lengthOfLongestSubstring(input1)
    print("Length of longest substring from input1:", longest)
    
    input2 = "bbbbb"
    longest = Solution().lengthOfLongestSubstring(input2)
    print("Length of longest substring from input2:", longest) 
    
    input3 = "pwwkew"   
    longest = Solution().lengthOfLongestSubstring(input3)
    print("Length of longest substring from input3:", longest)  
    
    input4 = ""              
    longest = Solution().lengthOfLongestSubstring(input4)
    print("Length of longest substring from input4:", longest)
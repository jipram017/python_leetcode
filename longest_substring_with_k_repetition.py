# Leetcode 395 - Longest Substring with At Least K Repeating Characters
# Level: MEDIUM
# O(N) time, O(1) space

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        
        longest, start = 0, 0
        split_chars = set()
        for c in s:
            if count[c] < k:
                split_chars.add(c)
        
        if not split_chars:
            return len(s)
        
        for i, c in enumerate(s):
            if c in split_chars:
                if i != start:
                    longest = max(longest, self.longestSubstring(s[start:i], k))
                start = i + 1
        
        if start != len(s):
            longest = max(longest, self.longestSubstring(s[start:len(s)], k))
            
        return longest

# Driver code
if __name__ == '__main__':
    input1 = "aaabb"
    k = 3
    longest = Solution().longestSubstring(input1, k)
    print("Longets substring from input1:", longest)
    
    input2 = "ababbc"
    k = 2
    longest = Solution().longestSubstring(input2, k)
    print("Longets substring from input2:", longest)        
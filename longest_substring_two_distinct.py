# Leetcode 159 - Longest Substring with At Most Two Distinct Characters
# Level: MEDIUM
# O(N) time, O(1) space

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        last_seen = {}
        longest, start  = 0, 0
        for i, c in enumerate(s):
            if c in last_seen or len(last_seen) < 2:
                if (i-start+1) > longest:
                    longest = i - start + 1
                    res = (start, i)
            else:
                for seen in last_seen:
                    if seen != s[i-1]:
                        start = last_seen[seen] + 1
                        del last_seen[seen]
                        break
                        
            last_seen[c] = i
        return longest, s[res[0]:res[1]+1]

# Driver code
if __name__ == '__main__':
    input1 = "abcadcacacacca"     
    longest = Solution().lengthOfLongestSubstringTwoDistinct(input1)
    print("Longest substring from input1:", longest)
    
        
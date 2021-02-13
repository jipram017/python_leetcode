# Leetcode 32 - Longest Valid Parentheses
# Level: HARD
# O(N) time, O(N) space

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i, c in enumerate(s):
          if c == ")" and stack and s[stack[-1]] == "(":
            stack.pop()
          else:
            stack.append(i)
    
        stack.append(len(s))
        max_length = stack[0]
    
        for index in range(1, len(stack)):
          max_length = max(max_length, stack[index] - stack[index-1] - 1)
        
        return max_length

# Driver code
if __name__ == '__main__':
    string1 = "(()"
    longest_parentheses = Solution().longestValidParentheses(string1)
    print("Length of the longest valid parenthesis substring")
    print(longest_parentheses)
    
    string2 = ")()())"
    longest_parentheses = Solution().longestValidParentheses(string2)
    print("Length of the longest valid parenthesis substring")
    print(longest_parentheses)
# Leetcode 131 - Palindrome Partitioning I
# Level: MEDIUM
# O(2**N) time, O(2**N) space

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions = []
        self.find_partition(s, [], partitions)
        return partitions
    
    def find_partition(self, s, partition, partitions):
        if not s:
            partitions.append(partition)
            
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if prefix == prefix[::-1]:
                self.find_partition(s[i:], partition + [s[:i]], partitions)

# Driver code
if __name__ == '__main__':
    input1 = "aab"
    partitions = Solution().partition(input1)
    print("All palindrome substrings from input1:", partitions)
    
    input2 = "a"
    partitions = Solution().partition(input2)
    print("All palindrome substrings from input2:", partitions)
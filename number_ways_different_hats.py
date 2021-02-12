# Leetcode 1434 - Number of Ways to Wear Different Hats to Each Other
# Level: HARD
# O(M*N*2**N) time, O(2**M) space where M=number of people, N=number of hats

from collections import defaultdict
from typing import List

class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        mod = 10**9 + 7
        N = len(hats)
        allHats = set()
        hatsToPeople = defaultdict(set)
        dp = [1] + [0 for _ in range((1<<N) - 1)]
        
        for person in range(N):
            for hat in hats[person]:
                hatsToPeople[hat].add(person)
                allHats.add(hat)
        
        for i in range(0, len(allHats), 1):
            for k in range(len(dp) - 1, -1, -1):
                for person in hatsToPeople.get(list(allHats)[i]):
                    if k & (1<<person) == 0:
                        newState = k | (1<<person)
                        dp[newState] = (dp[newState] + dp[k]) % mod 
        
        return dp[(1<<N) - 1]
                            
# Driver code
if __name__ == '__main__':
    hats1 = [[3,4],[4,5],[5]] 
    numberWays = Solution().numberWays(hats1)
    print("The minimum number of ways to wear different hats:", numberWays)      
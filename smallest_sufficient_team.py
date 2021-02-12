# Leetcode 1125 - Smallest Sufficient Team
# Level: HARD
# O(M * 2**N) time, O(2**N) space where M=number of people and N=number of required skills

from collections import defaultdict
from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        N = len(req_skills)
        skillsMap = defaultdict(int)
        for i in range(N):
            skillsMap[req_skills[i]] = 1<<i
        
        P = len(people)
        pSkillsMap = defaultdict(int)
        for i in range(P):
            s = 0
            for skill in people[i]:
                s = s | skillsMap[skill]
            pSkillsMap[i] = s
        
        dp = [[None] for _ in range(1<<N)]
        dp[0] = []
        for skillSet in range(len(dp)):
            curTeam = dp[skillSet]
            if curTeam == [None]:
                continue
            for person in range(P):
                mergedSkillSet = skillSet | pSkillsMap[person]
                if mergedSkillSet == skillSet:
                    continue
                if dp[mergedSkillSet] == [None] or len(dp[mergedSkillSet]) > len(dp[skillSet]) + 1:
                    dp[mergedSkillSet] = list(curTeam)
                    dp[mergedSkillSet].append(person)
        
        return dp[len(dp)-1]

# Driver code
if __name__ == '__main__':
    req_skills1 = ["algorithms","math","java","reactjs","csharp","aws"]
    people1 = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
    smallest_team = Solution().smallestSufficientTeam(req_skills1, people1)
    print("Smallest sufficient team:", smallest_team)
    
    req_skills2 = ["java","nodejs","reactjs"]
    people2 = [["java"],["nodejs"],["nodejs","reactjs"]]
    smallest_team = Solution().smallestSufficientTeam(req_skills2, people2)
    print("Smallest sufficient team:", smallest_team)
            
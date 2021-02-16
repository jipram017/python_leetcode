# Leetcode 97 - Interleaving Strings
# Level: HARD
# O(M*N) time, O(M*N) space

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        cache = [[None for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        return self.areInterwoven(s1, s2, s3, 0,0, cache)
    
    def areInterwoven(self, s1, s2, s3, i, j, cache):
        if cache[i][j] is not None:
            return cache[i][j]
        
        k = i + j
        if k == len(s3):
            return True
        
        if i < len(s1) and s3[k] == s1[i]:
            cache[i][j] = self.areInterwoven(s1, s2, s3, i + 1, j, cache)
            if cache[i][j]:
                return True
        elif j < len(s2) and s3[k] == s2[j]:
            cache[i][j] = self.areInterwoven(s1, s2, s3, i, j + 1, cache)
            return cache[i][j]
        
        return False

# A function to run test cases 
def test(A, B, C): 
    if (Solution().isInterleave(A, B, C)): 
        print(C, "is interleaved of", A, "and", B) 
    else:
        print(C, "is not interleaved of", A, "and", B)
       
# Driver Code 
if __name__ == '__main__': 
    test("XXY", "XXZ", "XXZXXXY") 
    test("XY", "WZ", "WZXY") 
    test("XY", "X", "XXY") 
    test("YX", "X", "XXY") 
    test("XXY", "XXZ", "XXXXZY") 
     
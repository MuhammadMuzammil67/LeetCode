class Solution:
    def maxScore(self, s: str) -> int:
        strLeft = 0
        strRight = 0
        highScore = 0
        
        for i in range(len(s)-1):
            strLeft = s[:i+1]
            strRight = s[i+1:]
            highScore = max(strLeft.count('0') + strRight.count('1'), highScore)

        return highScore
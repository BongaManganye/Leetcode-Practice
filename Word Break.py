#Word Break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1): #We will go through every string i in the length of the string starting at the end
            for w in wordDict: #Try every eord in the dictionary
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break #Break out of the for loop

        return dp[0]

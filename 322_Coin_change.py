class Solution:
    def coinChange(self,coins:List[int],ammount:int)->int:
        dp=[ammount+1]*(ammount+1)
        dp[0]=0
        
        for a in range(1,ammount+1):
            for c in coins:
                if a-c>=0:
                    dp[a]=min(dp[a],1+dp[a-c])
                    
        return dp[ammount] if dp[ammount]!=ammount+1 else -1          
        
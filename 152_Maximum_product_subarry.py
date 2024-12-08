class Solution:
    def maxProduct(self,nums:List[int])->int:
        resl=max(nums)
        curMin,curMax=1,1
        for n in nums:
            if n==0:
                curMax,curMax==1,1
                continue
            tmp=curMax*n
            curMax=max(n*curMax,n*curMin,n)
            curMin=min(n*tmp,n*curMin,n)
            res=max(res,curMax)
        return res   
                
            
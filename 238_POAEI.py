class Solution:
    def productExpectItself(self,nums:List[int]) -> List[int]:
        resl=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            resl[i]=prefix
            prefix=prefix*nums[i]
            
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            resl[i]=resl[i]*postfix
            postfix=postfix*nums[i]
        return resl        
    
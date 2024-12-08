class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]  # Initialize maxSub with the first element
        currentSum = 0    # Initialize currentSum to 0
        
        for n in nums:
            if currentSum < 0:
                currentSum = 0  # Reset currentSum if it drops below 0
            currentSum += n    # Add the current number to currentSum
            maxSub = max(maxSub, currentSum)  # Update maxSub if needed
        
        return maxSub

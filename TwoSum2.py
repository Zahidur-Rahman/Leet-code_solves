class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      prevmap={}
      for i,n in enumerate(numbers,start=1):
        diff=target-n
        if diff in prevmap:
            return[prevmap[diff],i]
        prevmap[n]=i
      return  

        
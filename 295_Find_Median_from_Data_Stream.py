import heapq


class MedianFinder:

    def __init__(self):
        self.small,self.large=[],[]

        
        
    
    def addNum(self, num: int) -> None:
        s=self.small
        l=self.large
        heapq.heappush(s,-1*num)
        if (s and l and (-1 *s[0])>l[0]):
            val=-1*heapq.heappop(s)
            heapq.heappush(l,val)
            
        if len(s)>len(l)+1:
            val=-1*heapq.heappop(s)
            heapq.heappush(l,val)
        if len(l)>len(s)+1:
            val=heapq.heappop(l)
            heapq.heappush(s,-1*val)            
                
            
             
        

    def findMedian(self) -> float:
        s=self.small
        l=self.large
        if len(s)>len(l):
            return -1*s[0]
        
        if len(l)>len(s):
            return l[0]
        
        return (-1 * s[0] + l[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
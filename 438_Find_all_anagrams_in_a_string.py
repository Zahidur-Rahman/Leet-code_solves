class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pDict={}
        sDict={}
        
        if len(p)>len(s):return []
        for i in range(len (p)):
            pDict[p[i]]=1+pDict.get(p[i],0)
            sDict[s[i]]=1+sDict.get(s[i],0)
        res=[0] if sDict==pDict else []
        l=0
        for r in range(len(p),len(s)):
            sDict[s[r]]=1+sDict.get(s[r],0)
            sDict[s[l]]-=1
            if sDict[s[l]]==0:
                sDict.pop(s[l])
            l=l+1
            if sDict==pDict:
                res.append(l)
        return res        
            
    
    
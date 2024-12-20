class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res=""
        for s in strs:
            res+=str(len(s))+"#"+s
        return res    
     

    def decode(self, str):
        i,res=0,[]
        while i<len(str):
            j=i
            while str[j]!="#":
                j+=1
            length=int(str[i:j])
            res.append(str[j+1:j+1+length])
            i=j+1+length
        return res        
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        
       
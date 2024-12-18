class Solution:
    def alienOrder(self, words: List[str]) -> str:
       
        adj = {c: set() for w in words for c in w}
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            
            # Check for invalid case (prefix issue)
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            # Build edges between characters
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])  # Add edge w1[j] -> w2[j]
                    break
        
        # Step 3: Topological sort using DFS
        visit = {}  
        res = []    
        
        def dfs(c):
            if c in visit:
                return visit[c]  # True means cycle detected
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):  # If a cycle is detected
                    return True
            visit[c] = False
            res.append(c)  
            return False
        
     
        for c in adj:
            if dfs(c):  # If a cycle is detected
                return ""
        
       
        res.reverse()
        return "".join(res)

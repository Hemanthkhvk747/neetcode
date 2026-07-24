class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}  
    
        for word in strs:
        
            key = "".join(sorted(word))   
        
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
    
    
        result = []
        for k in groups:
            result.append(groups[k])
        return result
        
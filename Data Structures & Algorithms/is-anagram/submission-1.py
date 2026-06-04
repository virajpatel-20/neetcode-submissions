class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        hash_map_t = {}
        n = len(s)
        m = len(t)
        for i in range(n):
            hash_map[s[i]]=hash_map.get(s[i], 0)+1
        for j in range(m):
            hash_map_t[t[j]]=hash_map_t.get(t[j], 0)+1
        if hash_map == hash_map_t:
            return True
        return False
        

        
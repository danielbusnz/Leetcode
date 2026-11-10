class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s.split()
       
        w2p = {}
        p2w = {}
        if len(pattern) != len(s):
            return False
        
        for a,b in zip(pattern,s):
            if a in w2p and w2p[a] != b:
                return False
            if b in p2w and p2w[b] != a:
                return False

            p2w[a] = b
            w2p[b] = a
        return True
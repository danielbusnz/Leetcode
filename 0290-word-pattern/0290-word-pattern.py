class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
       
        w2p = {}
        p2w = {}
        if len(pattern) != len(words):
            return False
        
        for a,b in zip(pattern, words):
            if a in p2w and p2w[a] != b:
                return False
            if b in w2p and w2p[b] != a:
                return False

            p2w[a] = b
            w2p[b] = a
        return True
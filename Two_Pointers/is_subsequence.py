class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t)>=len(s):
            for x in s:
                if x in t:
                    t = t[t.index(x)+1:]
                else:
                    return False
        else:
            return False
                
        return True
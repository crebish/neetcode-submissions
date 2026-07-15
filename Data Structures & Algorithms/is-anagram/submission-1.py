class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        myDictS = {}
        myDictT = {}

        for i in range(len(s)):
            myDictS[s[i]] = myDictS.get(s[i], 0) + 1
            myDictT[t[i]] = myDictT.get(t[i], 0) + 1

        return myDictS == myDictT

        
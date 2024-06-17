def isIsomorphic(self, s: str, t: str) -> bool:
        lenS=len(s)
        lenK=len(t)

        charCount=dict()
        for i in range (lenK):

            if s[i] in charCount:

                c=charCount[s[i]]

                if c!=t[i]:
                    return False
            
            elif t[i] not in charCount.values():

                charCount[s[i]]=t[i]
                
            else: 
                return False
        
        return True
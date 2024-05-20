def checkForComplete(s,k):

    lenS=len(s)
    lenK=len(k)

    charCount=dict()
    for i in range (lenK):

        if s[i] in charCount:

            c=charCount[s[i]]

            if c!=k[i]:
                return False
            
        elif k[i] not in charCount.values():

            charCount[s[i]]=k[i]
        else: 
            return False
        
    return True

if __name__=="__main__":

    s='paper'
    k='title'

    print(checkForComplete(s,k))




        
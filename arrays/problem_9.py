def singleOne(arr):
    n=len(arr)
    print(n)
    for i in range(n):
        count=0
        for j in range(n):
            if arr[i]==arr[j]:
                count+=1
                
        
        if count==1:
            return arr[i]
    #complexity will be O(N2)
        # with hashing and map ca also be solve but complexity will be 

def usingXOR(arr):
    n=len(arr)
    xor=0
    for i in range(n):
        xor=xor^arr[i]
    return xor
    #complexity will be time O(N)
    #space O(1)
        
if __name__=="__main__":
    elemets=[2,2,1]
    elemets2=[4,1,2,1,2]
    print(singleOne(elemets2))
    print(usingXOR(elemets2))
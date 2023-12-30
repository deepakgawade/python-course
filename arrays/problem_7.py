def missingNumber(arr):
    lenth=len(arr)
 

    if lenth==1:
        return arr[0] 
    #lastElement= arr[lenth-1]
    # sum can be calculate as sum of n natural number
    n=lenth+1

    sum1=(n*(n+1))//2
    print(sum1)
    #sum1=0
    sum2=0
    # for i in range(arr[0],lastElement+1):
    #     sum1=sum1+i
    for j in range(lenth):
        sum2=sum2+arr[j]
    pass
   
    num= sum1-sum2
    return num

def usingXOR(arr):
    n=len(arr)
    xor1=0
    xor2=0
    for i in range(n):
        xor1=xor1 ^ (i+1)
        xor2=xor2 ^ arr[i]
    xor1=xor1^(n+1)

    return xor1^xor2

    


def usingHashing(arr):
    length=len(arr)


    hashArr=[0 for i in range (1,arr[length-1]+1)]

    for i in arr:
        hashArr[i-1]=hashArr[i-1]+1



    for i in range(len(hashArr)):
    
        if hashArr[i]==0:
            return arr[i-1]+1

        


if __name__=="__main__":
    elements=[1,2,3,5]
    print(missingNumber(elements))
    print(usingHashing(elements))
    print(usingXOR(elements))
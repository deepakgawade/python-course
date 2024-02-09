
from collections import defaultdict
def brutesubarrayWithk(arr,k):
    n=len(arr)
    count=0
    for i in range(n):

        for j in range(n):

            xorr=0
            for x in range(i,j+1):
                xorr=xorr^arr[x]
            if xorr==k:
                count+=1
    return count

def bettersubarrayk(arr,k):
    n=len(arr)
    count=0
    for i in range(n):
        xorr=0

        for j in  range(i,n):
            xorr^=arr[j]


            if xorr==k:
                count+=1

    return count

def optimalSubbarrayk(arr,l):
    n=len(arr)
    count=0
    xr=0
    mpp= defaultdict(int)
    mpp[xr]=1
    for i in range(n):


        xr = xr^arr[i]

        x = xr ^ l 

        count = count+ mpp[x]
        mpp[xr] += 1
    return count



         



if __name__=="__main__":
    elemst=[4,2,2,6,4]
    k=6

    print(optimalSubbarrayk(elemst,k))


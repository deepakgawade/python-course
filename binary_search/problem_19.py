import math

def isSmallestDivisor(arr,divisor,limit):
    n=len(arr)
    sum=0
    for i in range(n):

        sum+=math.ceil(arr[i]/divisor)

    if sum<=limit:
        return True
    return False


def limitingDivisor(arr,limit):

    n=len(arr)

    maxi=float('-inf')

    for i in range(n):

        maxi=max(maxi,arr[i])

    low=1
    high=maxi

    while low<=high:
        mid = (low+high)//2

        if isSmallestDivisor(arr,mid,limit):

            high = mid-1

        else:

            low = mid+1

    if low <= limit:
        return low
    else: 
       return  -1

    # for j in range(1,maxi+1):

    #     if isSmallestDivisor(arr,j,limit):

    #         return j
    
if __name__=="__main__":
    elements=[8,4,2,3]
    limit=10

    print(limitingDivisor(elements,limit))







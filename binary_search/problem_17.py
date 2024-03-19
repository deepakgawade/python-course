import math

def findMax(arr):

    n = len(arr)

    maxi=float('-inf')

    for i in range(n):
        maxi=max(maxi, arr[i])

    return maxi


def calculateHours(arrX,hourly):

    n=len(arrX)
    total=0

    for i in range(n):

        total+=math.ceil(arrX[i]/hourly)

    return total

def minimRateToEatBananas(arrY,h):
    low=1
    high=findMax(arrY)

    while low<=high:
        mid =(low+high)//2

        hours=calculateHours(arrY,mid)

        if hours<=h:
            high=mid-1
        else:
            low=mid+1
    return low

    # for i in range(1,maxix+1):

    #     hours=calculateHours(arrY,i)

    #     if hours<=h:
    #         return i
    # return maxix


if __name__=="__main__":
    elements=[7,15,6,3]
    h=8

    print(minimRateToEatBananas(elements,h))





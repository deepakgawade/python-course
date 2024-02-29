import sys
def minimumElementRotated(arr):

    n=len(arr)
    low=0
    high=n-1

    ans=sys.maxsize
    while low<=high:

        mid= (low+high)//2

        if arr[low]<=arr[mid]:

            ans=min(ans, arr[low])

            low=mid+1
        else:
            ans=min(ans,arr[mid])
            high= mid-1

    return ans


if __name__=="__main__":

    elements= [4,5,1,2,3]
    elements2=[4,5,6,7,0,1,2,3]
    elements3=[3,4,5,1,2]

    print(minimumElementRotated(elements3))


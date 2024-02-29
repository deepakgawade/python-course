import sys
def timesSortedArrayRotated(arr):

    n= len(arr)
    low=0
    high=n-1

    ans=sys.maxsize
    ansindex=0

    while low<=high:

        mid=(low+high)//2

        if arr[low]<=arr[mid]:

            if arr[low]<ans:
                ans=arr[low]
                ansindex=low
            low=low+1
        else:
            if arr[mid]<ans:
                ans=arr[mid]
                ansindex=mid

            high=mid-1

    return ansindex

if __name__=="__main__":
    elements=[4,5,6,7,0,1,2,3]
    elements2=[3,4,5,1,2]

    print(f"{timesSortedArrayRotated(elements2)} Times")


def floorOfTarget(arr, target):
    n=len(arr)
    low=0

    high=n-1
    ans=-1

    while low<=high:

        mid = (low+high)//2

        if arr[mid]<= target:
            ans = arr[mid]

            low= mid+1

        else:
            high=mid -1

    return ans


def ceilOfTraget(arr, target):
    n=len(arr)
    low=0
    high= n-1

    ans=-1

    while low<= high:
        mid = (low +high)//2

        if arr[mid]>=target:

            ans = arr[mid]

            high=mid-1

        else:
            low =mid +1

    return ans

if __name__=="__main__":
    elslmets=[3, 4, 4, 7, 8, 10]
    elements2=[3, 4, 4, 7, 8, 10]


    target=8

    print(floorOfTarget(elslmets,target))
    print(ceilOfTraget(elslmets,target))

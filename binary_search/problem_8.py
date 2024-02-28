def firstOccurance(arr, target):

    n=len(arr)
    low= 0
    high=n-1
    ans=-1

    while low <= high:

        mid = (low+high)//2

        if arr[mid]>= target:

            ans=mid
            high=mid-1

        else:
            low=mid+1

    return ans

def lastOccurance(arr,target):

    n=len(arr)

    low=0
    high= n-1
    ans=-1

    while low<=high:

        mid= (low +high)//2

        if arr[mid]>target:

            ans=mid

            high=mid-1

        else:
            low=mid+1
    return ans-1

def firstAndLast(arr,target):
    n=len(arr)
    foc=firstOccurance(arr,target)
    if arr[foc]!=target or foc==n:
        return (-1,-1)
   
    up=lastOccurance(arr,target)
    return (foc, up)

if __name__=="__main__":

    elemts=[2, 4, 6, 8, 8, 8, 11, 13]
    target=6

    ans= firstAndLast(elemts,target)
    print(f"The fist occurance {ans[0]} and last occurance {ans[1]}")
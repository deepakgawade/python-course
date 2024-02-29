def searchRotatedArray(arr,target):
    n= len(arr)

    low=0
    high=n-1

    ans=-1

    while low<=high:

        mid= (low+high)//2

        if arr[mid]==target:
            ans = mid
        
        #now we will check for sorted part

        if arr[low]<=arr[mid]:
            ##remove one of part by moving pointer
            if arr[low]<=target and target<=arr[mid]:

                high= mid-1

            else:

                low=mid+1

        else:
             ##remove one of side by moving pointer
            if arr[mid]<=target and target<=arr[high]:

                low= mid+1

            else:

                high=high-1
    return ans


if __name__=="__main__":
    elements=[4,5,6,7,0,1,2,]
    target=3

    print(searchRotatedArray(elements,target))



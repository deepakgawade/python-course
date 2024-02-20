def  lowerBound(arr, target):
    n=len(arr)
    low=0
    high=n-1

    while low<=high:

        mid = (low+high)//2

        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            return arr[mid ] 
            #high=mid-1
        else:
            low=mid+1
if __name__=="__main__":
    elements=[3,5,8,15,19]
    elements2=[1,2,2,3]
    target=9
    print(lowerBound(elements2,2))

    

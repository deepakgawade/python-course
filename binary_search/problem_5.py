def  lowerBound(arr, target):
    n=len(arr)
    low=0
    high=n-1
    ans=target
    while low<=high:

        mid = (low+high)//2

   
        if arr[mid] >= target:
        
            ans= arr[mid]
            high=mid-1 
        else:
            low=mid+1
    return ans
    #TC log(n)
    #SC O(1)
if __name__=="__main__":
    elements=[3,5,8,15,19]
    elements2=[1,2,2,3,8,9,12,34,77,89,90]
    target=9
    print(lowerBound(elements,13))

    

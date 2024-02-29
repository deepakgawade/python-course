def peaksInArray(arr):

    n=len(arr)
    low=0
    high=n-1

    if n==1: return arr[0]

    if arr[0]>arr[1]: return arr[1]

    if arr[n-1] > arr[n-2]:return arr[ n-1]

    low=1
    high= n-2

    while low<=high:

        mid= (low+high)//2



        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            
            return arr[mid]
        
        elif arr[mid]>arr[mid-1]:

            low= mid+1

        else:

            high=mid-1

    return -1

if __name__=="__main__":
    elements=[1,2,3,4,5,6,7,8,5,1]

    print(peaksInArray(elements))

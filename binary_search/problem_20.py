def dayReqWithC(arr, capacity, days):

    n=len(arr)
    day=1
    load=0

    for i in range(n):

        if load+arr[i]>capacity:

            day+=1
            load=arr[i]
        else:
            load+=arr[i]


    if day<=days:
        return True
    else: 
        return False
    

def checkRequiredCapacity(arr,days):

    maxi=float('-inf')
    totalWeight=0
    n=len(arr)

    for i in range(n):
        maxi=max(maxi, arr[i])
        totalWeight+=arr[i]

    #can use binary search to reduce the time complexity
    for j in range(maxi,totalWeight+1):

        if dayReqWithC(arr,j,days):
            return j
    
    return -1

if __name__=="__main__":
    elements=[1,2,3,4,5,6,7,8,9,10]
    d=1
    print(checkRequiredCapacity(elements,d))


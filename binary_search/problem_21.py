def minimumDistanceForCow(arr, cows):
    n=len(arr)
    arr.sort()
    maxi, mini=arr[n-1],arr[0]
#here we can use binary search algo to reduce Time Complexity
    for i in range(1, maxi-mini):

        if canReplaceCow(arr,cows,i,n):
            continue
        else:
            return i-1
        
def canReplaceCow(arr,cows, i,n):

    countCows ,lastCows = 1,arr[0]

    for j in range(1,n):
        if arr[j]-lastCows>=i:
            countCows+=1
            lastCows=arr[j]

        if countCows==cows:

            return True
    
    

    return False
    
if __name__=="__main__":
    elements=[0,3,4,7,10,9]
    k=4

    print(minimumDistanceForCow(elements,k))





    
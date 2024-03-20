def isPossible(arr, day, m, k):
    n=len(arr)
    count=0
    noOfBuquet=0

    if n<m*k:
        return False

    for i in range(n):
        if arr[i]<=day:

            count+=1
        else:
            noOfBuquet+=count//k
            count=0

    noOfBuquet+=count//k

    return noOfBuquet>=m


def garden(arr, m,k):

    n=len(arr)
    if n<m*k:
        return -1

    mini = float('inf')
    maxi = float('-inf')

    for i in range(n):
        
        mini = min(mini, arr[i])
        maxi = max(maxi, arr[i])

    
    for j in range(mini, maxi+1):
        if isPossible(arr,j,m,k):
            return j
        
    return -1

if __name__=="__main__":
    arr=[7, 7, 7, 7, 13, 11, 12, 7]
    m=2
    k=3

    print(garden(arr,m,k))

    
    

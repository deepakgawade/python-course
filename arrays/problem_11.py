def countSumSubarray(arr,k):
    n= len(arr)
    left=0
    right=0

    count=0

    for i in range(n):
        for j in range(i,n):

            sum=0
            for p in range(j, j-i+1):
                sum+=arr[p]

            if sum== k:
                count+=1
    return count

    
if __name__=="__main__":
    elements=[3,1,2,4]
    print(countSumSubarray(elements, 6))
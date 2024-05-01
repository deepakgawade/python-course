def checkIfSumOfArray(arr, k, sum ):
      
    n=len(arr)
    divisions=1
    sumArray=0

    for j in range(n):

        if sumArray+arr[j]<=sum:
             sumArray+=arr[j]
             
        else:
             sumArray=arr[j]
             divisions+=1
    if divisions==k:
             return True
    return False
    





def minimumSumOfSubArray( arr, k):
        n=len(arr)

        mini  = arr[n-1]
        maxSum=0
        for i in range(n):
            maxSum+=arr[i]

        maxi = maxSum

        for sum in range(mini,maxi+1):
              if checkIfSumOfArray(arr, k, sum):
                    return sum

        return -1


if __name__=="__main__":
     
     elements=[1,2,3,4,5]
     k=3

     print(minimumSumOfSubArray(elements,k))


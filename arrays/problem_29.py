def betterApproch(arr):
    n=len(arr)
    maxx=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]

            if sum==0:
                maxx=max(maxx, j-i+1)

    return maxx


def optimalApproach(arr):
    #kadane's algorithm
    n=len(arr)
    mpp={}
    maxi=0
    sum=0
    for i in range(n):
        sum+=arr[i]
        if sum==0:
          maxi = i+1
        else:
            if sum in mpp:
                maxi=max(maxi, i - mpp[sum])
            else:
                mpp[sum]=i
    return maxi




if __name__=="__main__":
   elelmsy= [9, -3, 3, -1, 6, -5]

   print(betterApproch(elelmsy))
   print(optimalApproach(elelmsy))

 
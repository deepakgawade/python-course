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

if __name__=="__main__":
   elelmsy= [9, -3, 3, -1, 6, -5]

   print(betterApproch(elelmsy))

 
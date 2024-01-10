import sys

def kadensAlgo(arr):
    n=len(arr)
    sum=0
    max= -sys.maxsize-1

    start=0
    ansStart, ansEnd= -1,-1
    for i in range(n):
        if sum==0:
            start=i
        
        sum+=arr[i]

        if sum>max:
            max=sum
            ansStart=start
            ansEnd=i

        if sum<0:
            sum=0
    for i in range(ansStart,ansEnd+1):
        print(arr[i])

    return max
        
        


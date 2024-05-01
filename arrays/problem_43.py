def numbersSmallerThanEqualMid(mat,target):

    low=0
    high=len(mat)

    while low<=high:

        mid=(low+high)//2

        if mat[mid]<=target:
            low=mid+1
        else:
            high=mid-1

    return low
        

def medianOfMatrix(matrix):

    n=len(matrix)
    m=len(matrix[0])

    low=0
    high=10**9

   
    while low<=high:

        mid= (low+high)//2
        count=0

        for i in range(n):
            count+=numbersSmallerThanEqualMid(matrix[i],mid)

        if count<= (n*m)//2:
            low=mid+1
        else:
            high=mid-1
        
    return low
    
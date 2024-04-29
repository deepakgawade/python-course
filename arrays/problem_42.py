def maxElementColumn(matrix,n,m,col):
    maxValue=-1
    index=-1

    for i in  range(n):

        if matrix[i][col]>maxValue:
            maxValue=matrix[i][col]
            index=i

    return index


def peakElement(matrix):

    n=len(matrix)
    m=len(matrix[0])

    low =0
    high=m-1

    while low<=high:

        mid= (low+high)//2

        row=maxElementColumn(matrix,n,m,mid)

        left=-1
        right=-1

        if mid-1>=0: 
            left=matrix[row][mid-1]
        else:
            left=-1

        if mid+1<m: 
            right=matrix[row][mid+1]
        else:
            right=-1

        if matrix[row][mid]>left and matrix[row][mid]>right:
            return [row,mid]
        elif matrix[row][mid]<left:
            high=mid-1
        else:
            low=mid+1

    return [-1,-1]
        

if __name__=="__main__":
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    print(peakElement(matrix))
        
        
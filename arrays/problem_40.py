def findElement(matrix, n, m, k):

    low =0
    high=(n*m)-1

    while low<=high:


        mid= (low+high)//2
        row=mid//m
        col=mid%m

        if matrix[row][col]==k:
            return True
        
        elif matrix[row][col]<k:
             low=mid+1
        else: 
            high=mid-1

    return False

if __name__=="__main__":

    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    result = findElement(matrix,len(matrix),len(matrix[0]), 13)
    print("true" if result else "false")

def binSearch(matrix, k):

    low =0
    high=len(matrix)-1

    while low<=high:


        mid= (low+high)//2
      

        if matrix[mid]==k:
            return True
        
        elif matrix[mid]<k:
             low=mid+1
        else: 
            high=mid-1
    return False


def findElementMatrix(matrix,k):


    n=len(matrix)
    m=len(matrix[0])

    for i in range(n):

        if binSearch(matrix[i],k):
            return True
    return False


def optimizeSearch(matrix,k):
    
    n=len(matrix)
    m=len(matrix[0])
    row =0
    col=m-1

    while row <n and col>=0:

        if matrix[row][col]==k:
            return True
        elif matrix[row][col]>k:

            col-=1

        else:
            row+=1
    return False

if __name__=="__main__":
    matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
    ]

    result = optimizeSearch(matrix, 8)
    print("true" if result else "false")




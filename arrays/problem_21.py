
def markRow(matrix,n,m,i):

    for j in range(m):#mark -1 for all row
        if matrix[i][j]!=0:
            matrix[i][j]=-1

def markCol(matrix,n,m,j):

    for i in range(n):#mark -1 for all cloumn
        if matrix[i][j]!=0:
            matrix[i][j]=-1



def zeroMatrix(matrix, n,m):

    for i in range(n):
        for j in range(m):

            if matrix[i][j]==0:#check zero makr -1
                markCol(matrix,n,m,i)
                markRow(matrix,n,m,j)

    for i in range(n):#mark all -1 to zero
        for j in range(m):

            if matrix[i][j]==-1:
                matrix[i][j]=0

    return matrix  

    
if __name__=="__main__":
    matrix= [[1,1,1],[1,0,1],[1,1,1]]
    n=len(matrix)
    m=len(matrix[0])

    ans = zeroMatrix(matrix, n,m)

    for row in ans:
        for ele in row:
            print(ele, end=" ")
        print()

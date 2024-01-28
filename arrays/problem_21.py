
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

def betterZeroMatrix(matrix,n,m):
    row=[0]*n
    col=[0]*m

    for i in range(n):
        for j in range(m):

            if matrix[i][j]==0:#check zero makr -1
                row[i]=1
                col[j]=1

    for i in range(n):
        for j in range(m):

            if col[j] or row[i]:#check zero makr -1
               matrix[i][j]=0
    return matrix
               

def optimalZeroMatrix(matrix,n,m):
    # space complexity O(1)
    # time complexity 2O(n*m)
    # row=[0]*n-. matrix[..][0]

    # col=[0]*m->matrix[0][..]
    col0=1

    for i in range(n):
        for j in range(m):

            if matrix[i][j]==0:#check zero makr -1
                # row[i]=1
                # col[j]=1

                #mark ith row
                matrix[i][0]=0

                #mark jth col
                if j!=0:
                    
                    matrix[0][j]=0
                else:
                    col0=0
    
    for i in range(1,n):
        for j in range(1,m):

            if matrix[i][j]!=0:#check zero makr -1
               #check for row and column if it is zero
               if matrix[i][0]==0 or matrix[0][j]==0:
                   matrix[i][j]=0   

                
                    
    if matrix[0][0]==0:

        for j in range(n): 
                matrix[0][j]=0
    if col0==0:
            for i in range(n):
                matrix[i][0]=0 

    return matrix
         

    
if __name__=="__main__":
    matrix= [[1,1,1],[1,0,1],[1,1,1]]
    n=len(matrix)
    m=len(matrix[0])

    #ans = zeroMatrix(matrix, n,m)
    #ans =betterZeroMatrix(matrix,n,m)
    ans = optimalZeroMatrix(matrix,n,m)

    for row in ans:
        for ele in row:
            print(ele, end=" ")
        print()

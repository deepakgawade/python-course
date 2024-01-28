def antiRotate(matrix,n):

    rotatedarray=[[0 for i in range(n)] for j in range(n)]
    index=n-1
    for i in range(n):
        for j in range(n):
            rotatedarray[i][j]=matrix[j][index]    
        index-=1
    
    return rotatedarray

def optimizeRotate(matrix,n):

    for i in range(n):
        for j in range(i,n):
            #make a transpose row to colum
            matrix[i][j], matrix[j][i]=matrix[j][i] ,matrix[i][j]
    index=n-1
    for i in range(n):
        for j in range(n//2):
            #reverse all column
            matrix[j][i], matrix[index][i]=matrix[index][i],matrix[j][i]   
            index-=1
        index=n-1

    return matrix


if __name__=="__main__":
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    matrix2=   [[  4, 8, 12, 16 ],
        [3, 7, 11, 15 ],
        [2, 6, 10, 14 ],
        [1, 5, 9, 13 ]]

    rotated = optimizeRotate(matrix,3)
    print("Rotated Image")
    for i in range(len(rotated)):
        for j in range(len(rotated[0])):
            print(rotated[i][j], end=" ")
        print()


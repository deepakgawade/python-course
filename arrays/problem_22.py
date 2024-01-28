def rotate(matrix, n):

    rotatedarray=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            rotatedarray[j][n-i-1]=matrix[i][j]

    return rotatedarray
#time complexity is O(n2)
#space compelxity is also O(n2)

#to do in place we will take transpose and reverse each row
def optimizeRotate(matrix,n):
    for i in range(n):
        for j in range(i):
            #swap the elements rows to column
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix

if __name__=="__main__":
    matrix=[[1,2,3],[4,5,6],[7,8,9]]

   # rotated = rotate(matrix,3)
    rotated = optimizeRotate(matrix,3)
    print("Rotated Image")
    for i in range(len(rotated)):
        for j in range(len(rotated[0])):
            print(rotated[i][j], end=" ")
        print()
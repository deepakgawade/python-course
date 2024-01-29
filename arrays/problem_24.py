def spiral(matrix,):
    ans=[]
    n=len(matrix)#no. of rows
    m=len(matrix[0])#no. of col

    top=0
    left=0
    right=m-1
    bottom=n-1

    while left<=right or top<=bottom:
        for i in range(left,right+1): #left to right
            ans.append(matrix[top][i])
        top+=1# start from next eleemnt to avoid repetition

        for j in range(top,bottom+1):
            ans.append(matrix[j][right])
        right-=1
        if top<=bottom:
            for k in range(right, left-1,-1):
                ans.append(matrix[bottom][k])
            bottom-=1
        if left<=right:
            for k in range(bottom, top-1,-1):
                ans.append(matrix[k][left])
            left+=1
    return ans
    

mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
                     
ans = spiral(mat)

print(ans)
        
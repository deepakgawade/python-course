def loweBound(arr,n,x):
    low=0
    high=n-1

    ans=n

    while low<=high:
        mid= (low+high)//2
        if arr[mid]==x:
            ans=mid

            high = mid-1

        else:

            low = mid+1

    return ans



def rowWithMax(matrix,n,m):

    cnt_max=0
    index=-1

    for i in range(n):
        # get the number of 1's:
        cnt_ones = m - loweBound(matrix[i], m, 1)
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index


if __name__=="__main__":
    matrix = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
    n = 3
    m = 3
    print("The row with maximum no. of 1's is:", rowWithMax(matrix, n, m))
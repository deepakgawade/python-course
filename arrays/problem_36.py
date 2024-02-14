def bruteMaxProduct(arr):
    n=len(arr)
    maxx=float('-inf')
    for i in range(n):
    
        mul=1
        for j in range(i,n):
            mul*=arr[j]

            maxx=max(maxx, mul)
    return maxx

#nearly TC is O(N2)
#SC is O(1)

def optimalApproach(arr):
    n=len(arr)
    prefix=1
    sufix=1

    maxi=float('-inf')

    for i in range(n):

        if prefix==0: prefix=1
        if sufix==0:sufix=1

        prefix=prefix*arr[i]
        sufix=sufix*arr[n-i-1]

        maxi=max(maxi,max(prefix,sufix))
    return maxi


if __name__=="__main__":

    elements=[1,2,3,4,5,0]
    elements2=[1, 2, -3, 0, -4, -5]

    print(optimalApproach(elements))


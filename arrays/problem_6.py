def putZeroEnd(arr):
    n=len(arr)
    if len(arr)<=1:
        return
    

    for i in range(len(arr)):

        if arr[i]==0:
            temp=arr[i]
            for k in range(i,n-1):
                arr[k]=arr[k+1]
            arr[n-1]=temp

    print(arr)

        
if __name__=="__main__":
    elements=[1,0,2,3,0,4,0,1]
    elements2=[1,2,0,1,0,4,0]
    putZeroEnd(elements2)
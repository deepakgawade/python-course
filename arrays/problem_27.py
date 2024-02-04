def sumOfTiplet(arr,x):

    n=len(arr)
    stt=set()

    for i in range(n):

        for j in range(i+1,n):

            for k in range(j+1,n):

                if arr[i]+arr[j]+arr[k]==x:
                   temp=[arr[i],arr[j],arr[k]]
                   temp.sort()

                   stt.add(tuple(temp))
    
    ans= [list(item) for item in stt]


    return ans

if __name__=="__main__":
    nums=[-1,0,1,2,-1,-4]
    print(sumOfTiplet(nums,0))
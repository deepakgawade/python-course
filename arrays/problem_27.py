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

def betterSumTriplet(arr,x):
    n=len(arr)
    answer=[]
    sst2=set()
    

    for i in range(n):
        stt=set()
        for j in range(i+1,n):

            num= -(arr[i]+arr[j])
            if num in stt:
                ans=[arr[i],arr[j],num]
                ans.sort()
                sst2.add(tuple(ans))
            stt.add(arr[j])
            
    fromset=[list(item) for item in sst2]
    return fromset

    #O(n2)+O(nlogn)
    #O(N)+ 2*O(triplets)


def optimalTriplet(arr,x):
    n=len(arr)
    arr.sort()
    answer=[]
    for i in range(n):
        if i>0 and arr[i]==arr[i-1]:
            continue
        j=i+1
        k=n-1

        while j<k :
            sum= arr[i]+arr[j]+arr[k]
            if sum<x:
                j+=1

            elif sum> x:
                k-=1

            else:

                ans= [arr[i],arr[j], arr[k]]
                answer.append(ans) 
                j+=1
                k-=1
                while j<k and  arr[j]==arr[j-1]:
                    j+=1
                while j<k and arr[k]==arr[k+ 1]: 
                    k-=1

    return answer
                 
if __name__=="__main__":
    nums=[-1,0,1,2,-1,-4]
    print(optimalTriplet(nums,0))
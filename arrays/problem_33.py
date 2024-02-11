def bruteTwiceNumMissing(arr):
    n = len(arr)
    sum = 0
    #answer = [0]*(n)
 

    # for i in range(n):
    #     answer[arr[i]] =  
    zeroNum=0
    twiceNum=0
  
    for i in range(1,n+1):
        count=0
        for j in range(n):

            if i==arr[j]:
                count+=1

        if count==2:
            twiceNum=i

        elif count==0:
            zeroNum=i

        if zeroNum!=0 and twiceNum!=0:
            break

    print(zeroNum)
    print(twiceNum)

       
def betterApproach(arr):
    n=len(arr)
    hasarray=[0]*(n+1) 
    for i in range(n):

        hasarray[arr[i]]+=1
    print(hasarray)

    repeating=-1
    missing=-1
    for i in range(1,n+1):

        if hasarray[i]==2:
            repeating=i
        if hasarray[i]==0:
            missing=i


    print(repeating)
    print(missing)

    #TC O(N)+O(N)
    #SC O(N)
def otimalApproch(arr):
    n = len(arr)

    sn= (n*(n+1))/2
    sn2= (n*(n+1)*(2*n+1))/6
    s=0
    s2=0

    for i in range(n):
        s=s+arr[i]
        s2=s2+(arr[i]*arr[i])

    val1= s-sn
    val2=s2-sn2

    val2=val2/val1

    x=(val1+val2)/2
    y=x-val1

    print(f"{x}  {y}")




if __name__=="__main__":
    elements=[3,1,2,5,3]

    otimalApproch(elements)




def usingTwoPointer(arr, k):
    n=len(arr)
    i=0
    j=0
    sum=arr[0]
    maxLength=0
    while i<n:
        while i<=j and  sum >k:

            sum-=arr[i]
            i+=1
        if sum==k:
            maxLength= max(maxLength, j - i +1)

        j+=1
        if j<n: sum+=arr[j]
            
       
    return maxLength
    
        
    
def bruteLoggestArray( arr,total):
    length=len(arr)
    
    sunlength=0
    for i in range(length):
        for j in range(i,length):
            sum =0
            for k in range(i,j+1):
                sum = sum + arr[k]
               
            if sum == total :
                sunlength= max(sunlength , j-i+1)
                print(sunlength)

            
    return sunlength

#O(N**3)

if __name__=="__main__":

    elemets=[2,3,5,1,9]
   # value=  bruteLoggestArray(elemets,5)
    values1= usingTwoPointer(elemets,5)
    print(values1)
   # print(value)

    
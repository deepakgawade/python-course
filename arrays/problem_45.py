def isSubSequencePossible(arr,k):

    i,j=0,1

    n=len(arr)

    ans=[]

    arrayOfAnswer=[]

    if n%k!=0:
        return False

    while i<n and j<n:

        if len(ans)==0:
            ans.append(arr[i])
           
      
        elif ans[len(ans)-1]+1==arr[j]:
            ans.append(arr[j])
            j+=1

            if len(ans)==k:
                arrayOfAnswer.append(ans)
                ans=[]

 

        else:
            i=j
            j+=1
            print(i,j)
      



    if len(arrayOfAnswer)== n//k :
        return True
    
    else:
        return False
    

if __name__=="__main__":

    arr=[1,2,1,1,2,3]

    k=3

    print(isSubSequencePossible(arr,k))



        




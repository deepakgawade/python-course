def moveleftArray( arr,n):

    k=len(arr)-1

    temp=arr[0]

    for i in range(k):
        arr[i]=arr[i+1]

        

    arr[k]=temp

    
    print(arr)

def rotateArrleft(arr, d):
    #calculate rotaions
    n=len(arr)
    if d>n:
        d=d%n
    elif d==n:
        return


#copy elements to be rotated in temp
    temp= [arr[i] for i in range(0,d)]
  

#shifting
    for i in range(d, len(arr)):
        arr[i-d]=arr[i]
    
    k=0

    for j in range(len(arr)-d,len(arr)):
       
        arr[j] = temp[k]
        k+=1

    print(arr)
if __name__=="__main__":
    elemets=[1,2,3,4,5,6]
    #moveleftArray(elemets,1)
    rotateArrleft(elemets,)
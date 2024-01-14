def leadersInArray(arr):
    n=len(arr)
    ans=[]
  
    for i in range(n):
      
        isLead=True
        for j in range(i+1,n):
            if arr[i]<arr[j]:
 #s               print(arr)
                isLead=False
                break

        if isLead:
            print(arr[i])
        
    return ans
        

def optimizeLeaders(arr):
    n= len(arr)
    ans=[]
    max_ele=arr[n-1]
    ans.append(arr[n-1])
    for i in range(n-2,0,-1):
      
        if arr[i]>max_ele:
            ans.append(arr[i])
            max_ele=arr[i]
    
    print(ans)     
        

if __name__=="__main__":
    elements=[4,7,1,0]
    elements2=[10, 22, 12, 3, 0, 6]
    # print(leadersInArray(elements2))
    optimizeLeaders(elements2)
    # optimizeLeaders(elements2)



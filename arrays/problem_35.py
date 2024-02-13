def ms(arr, low , high):
    cnt=0
    if (low==high): return cnt

    mid= (low+high)//2

    cnt+= ms(arr, low,mid)
    cnt+=ms(arr, mid+1, high)
    cnt += countPairs(arr, low, mid, high) 
    cnt+=merge(arr, low ,mid, high)
    return cnt


def countPairs(arr, low ,mid,high):
    right=mid +1
    cnt =0

    for i in range(low, mid+1):
        while right<=high and arr[i]>2*arr[right]:
            right+=1
        cnt+=(right-(mid+1))
    return cnt

def merge(arr, low, mid, high):
    temp=[]
    left=low
    right=mid+1
    cnt = 0 
    print(f"arr before merge: {arr}")
    while(left<=mid and right<=high):
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
       
            right+=1

    while(left<=mid):
        temp.append(arr[left])
        left+=1

    while(right<=high):
        temp.append(arr[right])
        right+=1

    print(f"temp: {temp}")

    for i in range(low,high+1):
        print(f"i :{i} low:{low} high: {high}")
      
        arr[i]=temp[i-low]
    print(f"arr: {arr}")
    return cnt
def team(skills,n):
  
    print(  ms(skills,0,n-1))

if __name__=="__main__":
    elements=[1,3,2,3,1]
    team(elements,len(elements))




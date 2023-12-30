def consecutives(arr):
    n=len(arr)
    count=0
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            count+=1
    print(f"Consecutives of ones are {count}") 

if __name__=="__main__":
    elements=[1,1,0,1,1,1]
    consecutives(elements)
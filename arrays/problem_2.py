#second largest and second smallest

# use merge sort ort insertion sort then take second and second last elements

if __name__=="__main__":
    arr=[1,2,4,7,7,5]
    #arr= [19,54,86,10,8,43]
    arr.sort()
    print(arr)
    n=len(arr)

    smallest=0
    lasrgets=0

    s=0
    l=0

    for i in range(1,n-1):
        if arr[i]<arr[i+1]:
            s=i
            break

    smallest=arr[s]

    for k in range(n-1,0,-1):
        if arr[k-1]<arr[k]:
            l=k
            break


         
    lasrgets=arr[l-1]
  

    print(f"second largest {lasrgets} , second smallest {smallest} ")